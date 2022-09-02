from abc import ABC, abstractmethod
from enum import Enum
from common.grid_display import GridDisplay


class Color(Enum):
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 192)
    DARK_GREY = (64, 64, 64)
    LIGHT_GREY = (92, 92, 92)
    PURPLE = (128, 0, 128)


class Animation(ABC):
    def __init__(self, grid_display: GridDisplay, dim=(200, 200)):
        self._nd = grid_display.n
        self._md = grid_display.m
        if dim[0] < self._nd:
            self._n = self._nd
        else:
            self._n = dim[0]
        if dim[1] < self._md:
            self._m = self._md
        else:
            self._m = dim[1]
        self._grid_display = grid_display

    @property
    def dim(self) -> tuple:
        return self._n, self._m

    @property
    def n(self) -> int:
        return self._n

    @property
    def m(self) -> int:
        return self._m

    @abstractmethod
    def render(self):
        pass
