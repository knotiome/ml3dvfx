import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

node = hou.pwd()
geo = node.geometry()

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )
    def forward(self,x):
        x = self.flatten(x)
        logits = self.linear_relu(x)
        return logits
        
model_path = hou.pwd().parm('model').eval()

model = Net().to(device)
model.load_state_dict(torch.load(model_path, weights_only=True))
model.eval()