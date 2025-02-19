from typing import Tuple, Optional, Any


class Flattened2DList:
    def __init__(self, rows: int, cols: int, initial_value: Optional[Any] = None) -> None:
        self.rows = rows
        self.cols = cols
        self.data = [initial_value] * (rows * cols)

    def __index(self, index: Tuple[int, int]) -> int:
        row, col = index

        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of bounds")

        return row * self.cols + col

    def __getitem__(self, index: Tuple[int, int]) -> Optional[Any]:
        return self.data[self.__index(index)]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        self.data[self.__index(index)] = value

