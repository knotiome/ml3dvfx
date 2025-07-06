from pyray import *
import numpy as np
import random

init_window(1920, 1080, "Point Data")
set_target_fps(60)

camera = Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

COLORS = [RED, YELLOW, ORANGE, GREEN, BLUE, PURPLE]

def create_blob(num_points, seed=0, scaling_factor=10):
    np.random.seed(seed)
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    z = np.random.rand(num_points)













