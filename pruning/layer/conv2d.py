from torch import nn
from pruning.layer.abstract import LayerPruner


class Conv2dPruner(LayerPruner):
    def __init__(self) -> None:
        super().__init__()

    def prune(self, layer: nn.Module):
        # TODO implement
        pass
