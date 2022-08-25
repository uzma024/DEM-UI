import torch
import torch.nn as nn
import torch.functional as F

def model(im):
    tensor = torch.tensor(im)
    upsampled = F.interpolate(im, scale_factor=3, mode='bilinear')
    return upsampled.numpy()