from window import Window
from cell import Cell
from maze import Maze


def main():
    screen_width = 900
    screen_height = 700
    screen_margin = 50
    num_rows = 12
    num_cols = 16

    cell_size_x = (screen_width - 2 * screen_margin) // num_cols
    cell_size_y = (screen_height - 2 * screen_margin) // num_rows

    window = Window(screen_width, screen_height)

    Maze(screen_margin, screen_margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()

