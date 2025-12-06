import torch
import PIL
from PIL import Image
from torch import nn, save, load, cuda
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train  = datasets.MNIST(root='data', train=True, download=True, transform=ToTensor())
dataset = DataLoader(train, 32)

class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model=nn.Sequential(
            nn.Conv2d(1, 32, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(32, 64, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(64, 64, (3, 3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64*(28-6)*(28-6), 10),
        )

    def forward(self, x):
        return self.model(x) 

device = 'cuda' if cuda.is_available() else 'cpu'
print(f'Using device: {device}')

clf = ImageClassifier().to(device)
opt = Adam(clf.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

if __name__ == '__main__':
    with open('model.pt', 'rb') as f:
        clf.load_state_dict(load(f))
    
    img = Image.open('img_1.jpg')
    img = ToTensor()(img).unsqueeze(0).to(device)
    print(clf(img).argmax().item())
#     for epoch in range(10):
#         for batch in dataset:
#             X, y = batch
#             X, y = X.to(device), y.to(device)
#             yhat = clf(X)
#             loss = loss_fn(yhat, y)

#             opt.zero_grad()
#             loss.backward()
#             opt.step()

#         print(f'Epoch {epoch} Loss: {loss.item()}')
#     with open('model.pt', 'wb') as f:
#         save(clf.state_dict(), f)

# print("CUDA available:", cuda.is_available())
# print("CUDA device count:", cuda.device_count())
# print("CUDA device name:", cuda.get_device_name(0) if cuda.is_available() else "No CUDA device found")
# print("CUDA current device:", cuda.current_device() if cuda.is_available() else "No CUDA device found")
