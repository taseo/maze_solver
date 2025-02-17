from window import Window

from cell import Cell


def main():
    win = Window(800, 600)

    Cell(win).draw(50, 50, 100, 100)
    Cell(win).draw(100, 100, 150, 150)

    win.wait_for_close()


if __name__ == "__main__":
    main()

