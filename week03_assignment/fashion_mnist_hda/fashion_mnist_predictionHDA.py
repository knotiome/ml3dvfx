import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import pickle
from PIL import Image
import math



device = "cuda" if torch.cuda.is_available() else "cpu"
#print(f"Device is {device}")

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.30),
            nn.Linear(512, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.30),
            nn.Linear(512, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.30),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
        
def labelTranslate(labelNum):
    labelDict = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]  
    return labelDict[labelNum]       

def predict():
    import hou
    model_path = hou.pwd().parm('model_path').eval()
    model = Net().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    
    image_path = hou.pwd().parm('image_path').eval()
    image = Image.open(image_path).convert("L")
    
    transform = transforms.Compose([transforms.ToTensor(), transforms.Resize((28, 28))])
    image = transform(image).to(device)
    
    with torch.inference_mode():
        output = model(image)
        prediction = torch.argmax(output).item()
        
    labelTranslate(prediction)
    return(print(f"\nItem prediction: {labelTranslate(prediction)}"))

    
    
    
# IGNORE EVERYTHING BELOW...
    
#def serialize():
#    node = hou.pwd()
#    geo = node.geometry()
#    
#    prims = geo.prims()
#    num_rows = num_cols = int(math.sqrt(len(prims)))
#    print(num_rows)
#    
#    grid_matrix =[]
#    
#    for row in range(num_rows):
#        new_row = []
#        for col in range(num_cols):
#            prim_index = row * num_cols + col
#            prim = geo.prim(prim_index)
#            color = prim.attribValue("Cd")[0]
#            new_row.append(color)
#        grid_matrix.append(new_row)   
#            
#    print("")
#    for row in grid_matrix:
#        print(row)
#        
#    pickle_path = hou.pwd().parm('pkl_path').eval()
#    
#    with open(pickle_path, 'wb') as file:
#        pickle.dump(grid_matrix, file)
#    time.sleep(1)
#    
#
#
#def matrix_to_image():
#    with open('C:/Users/phile/development/ml3dvfx/week03_assignment/fashion_mnist_hda/matrix.pkl', 'rb') as file:
#        matrix = pickle.load(file)
#    np_matrix = np.array(matrix) * 255
#    np_matrix = np_matrix.astype(np.uint8)
#    
#    img = Image.fromarray(np_matrix, mode='L')
#    img.save('C:/Users/phile/development/ml3dvfx/week03_assignment/fashion_mnist_hda/matrix.png')
#    print(f"Image saved {output_path}")
#    
#    
#def texture_from_sketch():
#    serialize()
#    time.sleep(2)
#    matrix_to_image()
    