import sys
import torch
import pytorch_lightning as pl

from argparse import ArgumentParser
from torch.utils.data import DataLoader

from models.model import LitModel
from utils.constants import SAVEPATH 

GPUS = 1 if torch.cuda.is_available() else 0 


def train(args):
    train_data = CharDataset()
    train_dataloader = DataLoader(train_data, batch_size=args.batch_size, shuffle=True)
    val_data = CharDataset()
    val_dataloader = DataLoader(val_data, batch_size=args.batch_size, shuffle=True)
    
    model = LitModel()
    trainer = pl.Trainer.from_argparse_args(args)
    trainer.fit(
        model=model,
        train_dataloader=train_dataloader,
        val_dataloader=val_dataloader
    )

    test_dataset = CharDataset()
    test_dataloader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=True)
    train.test(
        model=model,
        dataloader=test_dataloader
    )

    print('Saving model.')
    torch.save(model.state_dict(), SAVEPATH)
