from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, p_1: Point, p_2: Point) -> None:
        self.p_1 = p_1
        self.p_2 = p_2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.p_1.x, self.p_1.y, self.p_2.x, self.p_2.y, fill=fill_color, width=2
        )

