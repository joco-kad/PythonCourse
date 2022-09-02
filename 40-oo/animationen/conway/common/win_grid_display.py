import graphics as g
import numpy as np
from common.grid_display import GridDisplay


class WinGridDisplay(GridDisplay):
    def __init__(self, color_map: dict = None, n=54, m=36):
        super().__init__(color_map, n, m)
        self._win = g.GraphWin('Lebe', 800, 800 * m / n, autoflush=False)
        self._win.setCoords(0.0, 0.0, n, m)
        self._win.setBackground('black')

    def update(self, color_grid: np.array):
        for n_pos in range(self._n):
            for m_pos in range(self._m):
                square = g.Rectangle(g.Point(n_pos + .1, m_pos - .1), g.Point(n_pos + .9, m_pos + .9))
                square.draw(self._win)
                color_entry = color_grid[n_pos, m_pos]
                if not isinstance(color_entry, np.void) and self.color_map is not None:
                    color = self.color_map.get(color_entry)
                else:
                    color = (0, 0, 0)
                square.setFill(g.color_rgb(color[0], color[1], color[2]))
        self._win.update()

    def clear(self):
        square = g.Rectangle(g.Point(0, 0), g.Point(self._n, self._m))
        square.draw(self._win)
        square.setFill(g.color_rgb(0, 0, 0))
        self._win.update()

    def update_pixel(self, n_pos: int, m_pos: int, color_map_key: int):
        square = g.Rectangle(g.Point(n_pos + .1, m_pos - .1), g.Point(n_pos + .9, m_pos + .9))
        square.draw(self._win)

        if self._color_map is None:
            return
        color_rgb: tuple = self._color_map.get(color_map_key)
        if color_rgb is not None:
            square.setFill(g.color_rgb(color_rgb[0], color_rgb[1], color_rgb[2]))
        self._win.update()
