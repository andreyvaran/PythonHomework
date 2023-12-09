import numpy as np
from typing import Any, Union


class MatrixOperationsMixin:

    def __add__(self, other: 'Matrix') -> 'Matrix':
        return Matrix(self.data + other.data)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        return Matrix(self.data - other.data)

    def __mul__(self, other: Union['Matrix', np.ndarray, int, float]) -> 'Matrix':
        if isinstance(other, Matrix):
            return Matrix(self.data * other.data)
        else:
            return Matrix(self.data * other)

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        return Matrix(self.data @ other.data)


class MatrixDisplayMixin:
    def __str__(self) -> str:
        return np.array2string(self.data)


class MatrixFileMixin:
    def to_file(self, file_path: str) -> None:
        with open(file_path, 'w') as f:
            f.write(str(self))


class Matrix(MatrixOperationsMixin, MatrixDisplayMixin, MatrixFileMixin):
    def __init__(self, data: Union[list, np.ndarray]):
        self._data = np.array(data)

    @property
    def data(self) -> np.ndarray:
        return self._data

    @data.setter
    def data(self, value: Union[list, np.ndarray]) -> None:
        self._data = np.array(value)


matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix1.to_file("a.txx")
matrix2.to_file("b.txx")
(matrix1 + matrix2).to_file("matrix+.txt")
(matrix1 - matrix2).to_file("matrix-.txt")
(matrix1 * matrix2).to_file("matrix*.txt")
(matrix1 @ matrix2).to_file("matrix@.txt")
