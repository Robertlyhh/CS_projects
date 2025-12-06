from datasets import load_dataset, DatasetDict
from torchvision import transforms
from PIL import Image
import torch
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import LabelEncoder

ds = load_dataset("AdrianoC/rubber-duck")

# Print available splits
print(ds)

print(ds['train']['image'])

print(ds['train']['description'])

# print(type|(ds['image']))
# print(type|(ds['description']))

exit()

# Define transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to model input size
    transforms.ToTensor(),          # Convert to PyTorch tensor
    transforms.Normalize(mean=[0.5], std=[0.5])  # Normalize images
])

# Custom function to process each image in the dataset
def process_image(example):
    try:
        image = example['image'].convert('RGB')
        example['pixel_values'] = transform(image)
        return example
    except Exception as e:
        print(f"Error processing example: {e}")
        return None

# Apply processing to the dataset
ds = ds.map(process_image)

# Encode labels
label_encoder = LabelEncoder()
all_labels = [example['description'] for example in ds['train']]
label_encoder.fit(all_labels)
ds = ds.map(lambda example: {'label': label_encoder.transform([example['description']])[0]})

# Split the dataset into training and validation sets
train_size = int(0.8 * len(ds['train']))
val_size = len(ds['train']) - train_size
train_data, val_data = random_split(ds['train'], [train_size, val_size])

# Convert Hugging Face dataset to PyTorch dataset
train_dataset = train_data.dataset.select(train_data.indices).with_format("torch", columns=["pixel_values", "label"])
val_dataset = val_data.dataset.select(val_data.indices).with_format("torch", columns=["pixel_values", "label"])

# Create DataLoaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)

# Example CNN
class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 112 * 112, num_classes)  # Adjust output size to match number of classes

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 16 * 112 * 112)  # Flatten for FC layer
        x = self.fc1(x)
        return x

# Instantiate model, loss, and optimizer
num_classes = len(label_encoder.classes_)
model = SimpleCNN(num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
epochs = 10
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    for batch in train_loader:
        inputs, labels = batch['pixel_values'], batch['label']
        
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Print debug information
        print(f"Epoch {epoch+1}, Batch Loss: {loss.item()}")
        print(f"Outputs: {outputs}")
        print(f"Labels: {labels}")

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}")

# Evaluation
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for batch in val_loader:
        inputs, labels = batch['pixel_values'], batch['label']
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

torch.save(model.state_dict(), "rubber_duck_model.pth")
