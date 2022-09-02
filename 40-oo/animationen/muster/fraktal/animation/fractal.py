import numpy as np
from common.grid_display import GridDisplay
from animation.animation import Animation


class Mandelbrot(Animation):
	_MAX_COUNT = 50

	def __init__(self, grid_display: GridDisplay, iterations=150):
		super().__init__(grid_display)
		self._color_map = {
			0: (0, 0, 0),
			1: (0, 0, 192),
			2: (92, 92, 92),
			3: (64, 64, 64),
			4: (128, 0, 128)
		}
		self._iterations = iterations
		self._dim_count = (0, self._MAX_COUNT)
		self._dim_color_map = (0, len(self._color_map) - 1)

	def render(self):
		self._grid_display.clear()
		self._grid_display.color_map = self._color_map
		x_cor = np.linspace(-2, 1, self._n)
		y_cor = np.linspace(-2, 2, self._m)
		x_len = len(x_cor)
		y_len = len(y_cor)
		for n_pos in range(x_len):
			for m_pos in range(y_len):
				c = complex(x_cor[n_pos], y_cor[m_pos])
				z = complex(0, 0)
				count = 0
				for k in range(self._iterations):
					z = (z * z) + c
					count = count + 1
					if abs(z) > 4 or count >= self._MAX_COUNT:
						break

				color_entry = round(np.interp(count, self._dim_count, self._dim_color_map))
				self._grid_display.update_pixel(n_pos, m_pos, color_entry)
