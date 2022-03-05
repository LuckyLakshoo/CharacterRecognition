import os
import torch
import pytorch_lightning as pl

from torch import nn

class LitModel(pl.LightningModule):
    def __init__(self, hparams) -> None:
        super().__init__()
        pass

    def forward(self, x):
        pass

    def training_step(self, batch, batch_idx):
        pass

    def training_step_end(self, *args, **kwargs) -> STEP_OUTPUT:
        #return super().training_step_end(*args, **kwargs)
        pass

    def training_epoch_end(self, outputs: EPOCH_OUTPUT) -> None:
        #return super().training_epoch_end(outputs)
        pass

    def validation_step(self, batch, batch_idx):
        pass

    def validation_step_end(self, *args, **kwargs) -> Optional[STEP_OUTPUT]:
        #return super().validation_step_end(*args, **kwargs)
        pass

    def validation_epoch_end(self, outputs: EPOCH_OUTPUT) -> None:
        #return super().validation_epoch_end(outputs)
        pass

    def test_step(self, *args, **kwargs) -> Optional[STEP_OUTPUT]:
        #return super().test_step(*args, **kwargs)
        pass

    def test_epoch_end(self, outputs: EPOCH_OUTPUT) -> None:
        #return super().test_epoch_end(outputs)
        pass

    def configure_optimizers(self):
        pass