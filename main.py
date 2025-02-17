from window import Window

from line import Line
from point import Point


def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(10,10), Point(40, 40)), "red")
    win.draw_line(Line(Point(50,50), Point(80, 80)), "blue")
    win.draw_line(Line(Point(90,90), Point(120, 120)), "green")
    
    win.wait_for_close()


if __name__ == "__main__":
    main()

