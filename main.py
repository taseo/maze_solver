from window import Window

from cell import Cell


def main():
    win = Window(800, 600)

    c_1 = Cell(win)
    c_2 = Cell(win)
    c_3 = Cell(win)

    c_1.draw(50, 50, 100, 100)
    c_2.draw(100, 100, 150, 150)
    c_3.draw(150, 150, 200, 200)

    c_1.draw_move(c_2)
    c_2.draw_move(c_3, True)

    win.wait_for_close()


if __name__ == "__main__":
    main()

