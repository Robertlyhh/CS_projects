import torch
from torchvision import transforms
from PIL import Image
from ts.torch_handler.base_handler import BaseHandler
import io
from torch import nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 112 * 112, num_classes)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 16 * 112 * 112)
        x = self.fc1(x)
        return x

class RubberDuckHandler(BaseHandler):
    def __init__(self):
        super(RubberDuckHandler, self).__init__()
        self.model = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5], std=[0.5])
        ])

    def initialize(self, context):
        model_dir = context.system_properties.get("model_dir")
        self.model = SimpleCNN(num_classes=2)  # Adjust num_classes as needed
        self.model.load_state_dict(torch.load(f"{model_dir}/rubber_duck_model.pth", map_location=self.device))
        self.model.to(self.device)
        self.model.eval()

    def preprocess(self, data):
        image = data[0].get("data") or data[0].get("body")
        image = Image.open(io.BytesIO(image)).convert('RGB')
        image = self.transform(image).unsqueeze(0).to(self.device)
        return image

    def inference(self, data, *args, **kwargs):
        with torch.no_grad():
            outputs = self.model(data)
            _, predicted = torch.max(outputs, 1)
        return predicted.cpu().numpy().tolist()

    def postprocess(self, data):
        return [{"class_index": d} for d in data]