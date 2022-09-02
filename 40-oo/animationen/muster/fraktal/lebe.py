from common.win_grid_display import WinGridDisplay, GridDisplay
from animation.animation import Animation
from animation.conway import Conway
from animation.fractal import Mandelbrot


def loop(grid_display: GridDisplay):
    animations: Animation = \
        [Mandelbrot(grid_display), Conway(grid_display, grid_display.dim)]

    while True:
        for animation in animations:
            animation.render()


def main():
    loop(WinGridDisplay(n=200, m=200))


if __name__ == '__main__':
    main()
