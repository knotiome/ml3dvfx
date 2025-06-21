import os
import pandas as pd
from PIL import Image
import torch
from torchvision import transforms
from torch.utils.data import Dataset

class NYUDepthDataset(Dataset):
    def __init__(self, csv_file, transform=None): 
        self.data = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_path = self.data.iloc[idx, 0]
        depth_path = self.data.iloc[idx, 1]

        image = Image.open(img_path).convert('RGB')
        depth = Image.open(depth_path).convert('L')

        sample = {"image": image, "depth": depth}

        if self.transform:
            sample = self.transform(sample)
            
        return sample
    
class NYUDepthTransform:
    def __init__(self, img_size=(224,224)):
        self.img_transform = transforms.Compose
    












