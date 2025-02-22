import time
import random
from typing import Optional, List, Tuple

from window import Window
from cell import Cell
from grid_2d import Grid2D


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
        seed: Optional[int] = None,
    ) -> None:
        self.x_1 = x_1
        self.y_1 = y_1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.__window = window

        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self) -> None:
        self.__cells = Grid2D(self.num_rows, self.num_cols)

        for y in range(self.num_rows):
            for x in range(self.num_cols):
                self.__cells[x, y] = Cell(self.__window)
                self.__draw_cell(x, y)

    def __draw_cell(self, x_a: int, x_b: int) -> None:
        x = self.x_1 + (x_a * self.cell_width)
        y = self.y_1 + (x_b * self.cell_height)

        self.__cells[x_a, x_b].draw(x, y, x + self.cell_width, y + self.cell_height)

        self.__animate()

    def __break_entrance_and_exit(self) -> None:
        first_x, first_y = (0, 0)
        last_x, last_y = (self.num_cols - 1, self.num_rows - 1)

        self.__cells[first_x, first_y].has_top_wall = False
        self.__draw_cell(first_x, first_y)

        self.__cells[last_x, last_y].has_bottom_wall = False
        self.__draw_cell(last_x, last_y)

    def __get_adjacent_unvisited_cells(self, x: int, y: int) -> List[Tuple[int, int]]:
        adjacent_unvisited_cells: List[Tuple[int, int]] = []

        # top
        if y > 0 and not self.__cells[x, y - 1].visited:
            adjacent_unvisited_cells.append((x, y - 1))

        # right
        if x < self.num_cols - 1 and not self.__cells[x + 1, y].visited:
            adjacent_unvisited_cells.append((x + 1, y))

        # bottom
        if y < self.num_rows - 1 and not self.__cells[x, y + 1].visited:
            adjacent_unvisited_cells.append((x, y + 1))

        # left
        if x > 0 and not self.__cells[x - 1, y].visited:
            adjacent_unvisited_cells.append((x - 1, y))

        return adjacent_unvisited_cells

    def __knock_adjacent_wall(
        self, x: int, y: int, target_x: int, target_y: int
    ) -> None:
        # top
        if y > target_y:
            self.__cells[x, y].has_top_wall = False
            self.__cells[target_x, target_y].has_bottom_wall = False

            return

        # right
        if x < target_x:
            self.__cells[x, y].has_right_wall = False
            self.__cells[target_x, target_y].has_left_wall = False

            return

        # bottom
        if y < target_y:
            self.__cells[x, y].has_bottom_wall = False
            self.__cells[target_x, target_y].has_top_wall = False

            return

        # left
        if x > target_x:
            self.__cells[x, y].has_left_wall = False
            self.__cells[target_x, target_y].has_right_wall = False

            return

    def __break_walls_r(self, x: int, y: int) -> None:
        self.__cells[x, y].visited = True

        while True:
            to_visit = self.__get_adjacent_unvisited_cells(x, y)

            if not to_visit:
                return self.__draw_cell(x, y)

            target_x, target_y = to_visit[random.randrange(len(to_visit))]

            self.__knock_adjacent_wall(x, y, target_x, target_y)

            self.__break_walls_r(target_x, target_y)

    def __reset_cells_visited(self) -> None:
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                self.__cells[x, y].visited = False

    def __animate(self) -> None:
        self.__window.redraw()

        time.sleep(0.05)

    def __solve_r(self, x: int, y: int) -> bool:
        self.__animate()

        self.__cells[x, y].visited = True

        if x == self.num_cols - 1 and y == self.num_rows - 1:
            return True

        directions = self.__get_adjacent_unvisited_cells(x, y)

        for direction in directions:
            target_x, target_y = direction

            # up
            if y > target_y:
                if (not self.__cells[x, y].has_top_wall and not self.__cells[target_x, target_y].has_bottom_wall):
                    self.__cells[x, y].draw_move(self.__cells[target_x, target_y])

                    if self.__solve_r(target_x, target_y):
                        return True
                    else:
                        self.__cells[x, y].draw_move(self.__cells[target_x, target_y], True)

            # right
            if x < target_x:
                if (not self.__cells[x, y].has_right_wall and not self.__cells[target_x, target_y].has_left_wall):
                    self.__cells[x, y].draw_move(self.__cells[target_x, target_y])

                    if self.__solve_r(target_x, target_y):
                        return True
                    else:
                        self.__cells[x, y].draw_move(self.__cells[target_x, target_y], True)

            # down
            if y < target_y:
                if (not self.__cells[x, y].has_bottom_wall and not self.__cells[target_x, target_y].has_top_wall):
                    self.__cells[x, y].draw_move(self.__cells[target_x, target_y])

                    if self.__solve_r(target_x, target_y):
                        return True
                    else:
                        self.__cells[x, y].draw_move(self.__cells[target_x, target_y], True)

            # left
            if x > target_x:
                if (not self.__cells[x, y].has_left_wall and not self.__cells[target_x, target_y].has_right_wall):
                    self.__cells[x, y].draw_move(self.__cells[target_x, target_y])

                    if self.__solve_r(target_x, target_y):
                        return True
                    else:
                        self.__cells[x, y].draw_move(self.__cells[target_x, target_y], True)

        return False

    def solve(self) -> None:
        self.__solve_r(0, 0)

