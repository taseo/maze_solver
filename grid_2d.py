from typing import Tuple, Any


class Grid2D:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.data = [None] * (rows * cols)

    def __index(self, index: Tuple[int, int]) -> int:
        x, y = index

        if not (0 <= x < self.cols and 0 <= y < self.rows):
            raise IndexError("Index out of bounds")

        return y * self.cols + x

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        return self.data[self.__index(index)]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        self.data[self.__index(index)] = value

