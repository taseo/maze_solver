from window import Window
from line import Line
from point import Point


class Cell:
    def __init__(self, window: Window) -> None:
        self.__window = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.x_1 = 0
        self.y_1 = 0
        self.x_2 = 0
        self.y_2 = 0

        self.visited = False

    def draw(self, x_1: int, y_1: int, x_2: int, y_2: int) -> None:
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

        self.__window.draw_line(
            Line(
                Point(x_1, y_1),
                Point(x_1, y_2),
            ),
            "black" if self.has_left_wall else "white",
        )

        self.__window.draw_line(
            Line(
                Point(x_2, y_1),
                Point(x_2, y_2),
            ),
            "black" if self.has_right_wall else "white",
        )

        self.__window.draw_line(
            Line(
                Point(x_1, y_1),
                Point(x_2, y_1),
            ),
            "black" if self.has_top_wall else "white",
        )

        self.__window.draw_line(
            Line(
                Point(x_2, y_2),
                Point(x_1, y_2),
            ),
            "black" if self.has_bottom_wall else "white",
        )

    def get_center_point(self):
        return Point((self.x_1 + self.x_2) // 2, (self.y_1 + self.y_2) // 2)

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        self.__window.draw_line(
            Line(
                self.get_center_point(),
                to_cell.get_center_point(),
            ),
            "gray" if undo else "red",
        )
