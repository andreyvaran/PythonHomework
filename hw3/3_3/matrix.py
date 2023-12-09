import numpy as np


class MatrixHashMixin:
    def __hash__(self) -> int:
        """
        Simple hash function for a matrix.
        This hash function calculates the sum of all elements in the matrix.
        """
        return int(np.sum(self.data))


class MatrixOperationsMixin(MatrixHashMixin):
    _cache: dict[tuple[int, int], 'Matrix'] = {}

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        hash_self = hash(self)
        hash_other = hash(other)
        if (hash_self, hash_other) in self._cache:
            return self._cache[(hash_self, hash_other)]

        result = Matrix(self.data @ other.data)
        self._cache[(hash_self, hash_other)] = result
        return result


class MatrixDisplayMixin:
    def __str__(self) -> str:
        return np.array2string(self.data)


class MatrixFileMixin:
    def to_file(self, file_path: str) -> None:
        with open(file_path, 'w') as f:
            f.write(str(self))


class Matrix(MatrixOperationsMixin, MatrixDisplayMixin, MatrixFileMixin):
    def __init__(self, data: list | np.ndarray):
        self._data = np.array(data)

    @property
    def data(self) -> np.ndarray:
        return self._data

    @data.setter
    def data(self, value: list | np.ndarray) -> None:
        self._data = np.array(value)


def find_collision() -> tuple[Matrix, Matrix, Matrix, Matrix]:
    np.random.seed(111001)

    while True:
        A = Matrix(np.random.randint(0, 10, (10, 10)))
        C = Matrix(np.random.randint(0, 10, (10, 10)))

        if hash(A) == hash(C) and not np.array_equal(A.data, C.data):
            B = D = Matrix(np.random.randint(0, 10, (10, 10)))
            return A, B, C, D


A, B, C, D = find_collision()

AB = A @ B
CD = C @ D

A.to_file('A.txt')
B.to_file('B.txt')
C.to_file('C.txt')
D.to_file('D.txt')
AB.to_file('AB.txt')
CD.to_file('CD.txt')

with open('hash.txt', 'w') as f:
    f.write(f"Hash of AB: {hash(AB)}\n")
    f.write(f"Hash of CD: {hash(CD)}\n")
