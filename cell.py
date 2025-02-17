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

    def draw(self, x_1: int, y_1: int, x_2: int, y_2: int) -> None:
        if self.has_left_wall:
            self.__window.draw_line(
                Line(
                    Point(x_1, y_1),
                    Point(x_1, y_2),
                ),
                "black",
            )

        if self.has_right_wall:
            self.__window.draw_line(
                Line(
                    Point(x_2, y_1),
                    Point(x_2, y_2),
                ),
                "black",
            )

        if self.has_top_wall:
            self.__window.draw_line(
                Line(
                    Point(x_1, y_1),
                    Point(x_2, y_1),
                ),
                "black",
            )

        if self.has_bottom_wall:
            self.__window.draw_line(
                Line(
                    Point(x_2, y_2),
                    Point(x_1, y_2),
                ),
                "black",
            )

