import numpy as np
from abc import ABC, abstractmethod


class GridDisplay(ABC):
    GRID_DT = [('r', np.uint8), ('g', np.uint8), ('b', np.uint8)]

    def __init__(self, color_map: dict, n: int, m: int):
        self._n = n
        self._m = m
        self._color_map = color_map

    @property
    def dim(self):
        return self._n, self._m

    @property
    def n(self):
        return self._n

    @property
    def m(self):
        return self._m

    @property
    def color_map(self):
        return self._color_map

    @color_map.setter
    def color_map(self, color_map: dict):
        self._color_map = color_map

    @abstractmethod
    def update(self, color_grid: np.array):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def update_pixel(self, n_pos: int, m_pos: int, color_map_key: int):
        pass
