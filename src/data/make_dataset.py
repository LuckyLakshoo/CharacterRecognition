import os
import torch

from torch.utils.data import Dataset
from torchvision.transforms import ToTensor


class CharDataset(Dataset):
    def __init__(self, annot, root, transform=None):
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass