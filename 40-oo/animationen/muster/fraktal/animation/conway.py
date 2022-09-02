from abc import ABC, abstractmethod
from enum import Enum
from queue import Queue
from random import randrange

import numpy as np

from animation.animation import Animation, Color
from common.grid_display import GridDisplay


def calc_total(n_pos, m_pos, n, m, status_grid: np.array):
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = True
    if n_pos == 0:
        s3 = False
        s5 = False
        s6 = False
    if m_pos == 0:
        s1 = False
        s5 = False
        s7 = False
    if n_pos >= n - 1:
        s4 = False
        s7 = False
        s8 = False
    if m_pos >= m - 1:
        s2 = False
        s6 = False
        s8 = False

    total = 0
    if s1 and status_grid[n_pos, m_pos - 1]:
        total += 1
    if s2 and status_grid[n_pos, m_pos + 1]:
        total += 1
    if s3 and status_grid[n_pos - 1, m_pos]:
        total += 1
    if s4 and status_grid[n_pos + 1, m_pos]:
        total += 1
    if s5 and status_grid[n_pos - 1, m_pos - 1]:
        total += 1
    if s6 and status_grid[n_pos - 1, m_pos + 1]:
        total += 1
    if s7 and status_grid[n_pos + 1, m_pos - 1]:
        total += 1
    if s8 and status_grid[n_pos + 1, m_pos + 1]:
        total += 1

    return total


class Rule(ABC):
    def __init__(self, n, m):
        self._n = n
        self._m = m

    @abstractmethod
    def apply(self, n_pos, m_pos, old_status_grid: np.array, new_status_grid: np.array):
        pass


class StandardRule(Rule):
    def __init__(self, n, m):
        Rule.__init__(self, n, m)
        self._n = n
        self._m = m

    def apply(self, n_pos, m_pos, old_status_grid: np.array, new_status_grid: np.array):
        total = calc_total(n_pos, m_pos, self._n, self._m, old_status_grid)

        if old_status_grid[n_pos, m_pos]:
            if (total < 2) or (total > 3):
                new_status_grid[n_pos, m_pos] = False
        else:
            if total == 3:
                new_status_grid[n_pos, m_pos] = True


class HighlifeRule(Rule):
    def __init__(self, n, m):
        Rule.__init__(self, n, m)
        self._n = n
        self._m = m

    def apply(self, n_pos, m_pos, old_status_grid: np.array, new_status_grid: np.array):
        total = calc_total(n_pos, m_pos, self._n, self._m, old_status_grid)

        if old_status_grid[n_pos, m_pos]:
            if (total < 2) or (total > 3):
                new_status_grid[n_pos, m_pos] = False
        else:
            if total == 3 or total == 6:
                new_status_grid[n_pos, m_pos] = True


class ColorMap(Enum):
    COLOR_MAP_OFF = 0
    COLOR_MAP_STALE1 = 1
    COLOR_MAP_STALE2 = 2
    COLOR_MAP_STALE3 = 3
    COLOR_MAP_ON = 4


class Conway(Animation):
    _STALE1 = 5
    _STALE2 = 10
    _STALE3 = 15

    _STALE_LIMIT = _STALE3

    _VALS = [False, True]

    def __init__(self, grid_display: GridDisplay, dim=(200, 200), p=None):
        super().__init__(grid_display, dim)
        if p is None:
            p = [0.8, 0.2]
        self._p = p
        self._status_grid = None

        wn = self._n // 2 - self._nd // 2
        wm = self._m // 2 - self._md // 2
        self._win = (wn, wm, wn + self._nd, wm + self._md)

        self._old_status_grids = Queue()

        self._color_map = {
            ColorMap.COLOR_MAP_OFF.value: Color.BLACK.value,
            ColorMap.COLOR_MAP_STALE1.value: Color.BLUE.value,
            ColorMap.COLOR_MAP_STALE2.value: Color.LIGHT_GREY.value,
            ColorMap.COLOR_MAP_STALE3.value: Color.DARK_GREY.value,
            ColorMap.COLOR_MAP_ON.value: Color.PURPLE.value
        }

    def _random_grid(self):
        return np.random.choice(self._VALS, self._n * self._m, p=self._p).reshape(self._n, self._m)

    def _gen_from_color_grid(self, color_grid: np.array):
        status_grid = np.zeros((self._n, self._m), dtype=int)
        wn = self._win[0]
        wm = self._win[1]
        rand_limit = randrange(10, 255)
        empty = True
        for n_pos in range(self._nd):
            for m_pos in range(self._md):
                rgb: tuple = color_grid[n_pos, m_pos]
                on = rgb[0] + rgb[1] + rgb[2] > rand_limit
                if on:
                    empty = False
                status_grid[n_pos + wn, m_pos + wm] = on
        if empty:
            return None
        else:
            return status_grid

    def _calc_color_grid(self, color_grid: np.array):
        alive = False
        wn = 0
        for n_pos in range(self._win[0], self._win[2]):
            wm = 0
            for m_pos in range(self._win[1], self._win[3]):
                cm: ColorMap = self._get_color_map(n_pos, m_pos)
                if cm == ColorMap.COLOR_MAP_ON:
                    alive = True
                color_grid[wn, wm] = cm.value
                wm = wm + 1
            wn = wn + 1
        return alive

    def _get_color_map(self, n_pos, m_pos) -> ColorMap:
        if not self._status_grid[n_pos, m_pos]:
            return ColorMap.COLOR_MAP_OFF

        active_cell = 0
        for old_status_grid in self._old_status_grids.queue:
            if old_status_grid[n_pos, m_pos]:
                active_cell += 1

        if active_cell < self._STALE1:
            return ColorMap.COLOR_MAP_ON
        if active_cell < self._STALE2:
            return ColorMap.COLOR_MAP_STALE1
        if active_cell < self._STALE3:
            return ColorMap.COLOR_MAP_STALE2
        return ColorMap.COLOR_MAP_STALE3

    def _update(self, rule: Rule):
        status_grid = self._status_grid
        new_status_grid = self._status_grid.copy()
        n = self._n
        m = self._m
        for n_pos in range(n):
            for m_pos in range(m):
                rule.apply(n_pos, m_pos, status_grid, new_status_grid)

        self._old_status_grids.put(status_grid)
        if self._old_status_grids.qsize() > self._STALE_LIMIT:
            self._old_status_grids.get()
        self._status_grid = new_status_grid

    def render(self):
        self._grid_display.clear()
        self._grid_display.color_map = self._color_map
        self._status_grid = self._random_grid()
        if self._status_grid is None:
            return
        self._old_status_grids = Queue()

        rules = (StandardRule(self._n, self._m), HighlifeRule(self._n, self._m))

        color_grid = np.zeros((self._nd, self._md), dtype=np.uint8)
        while True:
            self._update(rules[randrange(0, len(rules))])
            active = self._calc_color_grid(color_grid)
            self._grid_display.update(color_grid)
            if not active:
                break
