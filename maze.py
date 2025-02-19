import time

from window import Window
from cell import Cell
from flattened_2d_list import Flattened2DList


class Maze:
    def __init__(
        self,
        x_1: int,
        y_1: int,
        num_rows: int,
        num_cols: int,
        cell_width: int,
        cell_height: int,
        window: Window,
    ) -> None:
        self.x_1 = x_1
        self.y_1 = y_1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.__window = window

        self.__create_cells()

    def __create_cells(self) -> None:
        self.__cells = Flattened2DList(self.num_rows, self.num_cols, Cell(self.__window))

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.__draw_cell(row, col)

    def __draw_cell(self, row: int, col: int) -> None:
        x = self.x_1 + (col * self.cell_width)
        y = self.y_1 + (row * self.cell_height)

        self.__cells[row, col].draw(x, y, x + self.cell_width, y + self.cell_height)

        self.__animate()

    def __animate(self) -> None:
        self.__window.redraw()

        time.sleep(0.05)

