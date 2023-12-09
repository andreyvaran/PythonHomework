class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of same dimensions for addition")

        result = []
        for i in range(self.rows):
            row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            result.append(row)

        return Matrix(result)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of same dimensions for component-wise multiplication")

        result = []
        for i in range(self.rows):
            row = [self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)]
            result.append(row)

        return Matrix(result)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for matrix multiplication")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum_product = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols))
                row.append(sum_product)
            result.append(row)

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


import numpy as np

np.random.seed(0)
data1: list = np.random.randint(0, 10, (2, 2)).tolist()
data2: list = np.random.randint(0, 10, (2, 2)).tolist()

matrix1 = Matrix(data1)
matrix2 = Matrix(data2)

with open('a.txt', 'w') as f:
    f.write(str(matrix1))

with open('b.txt', 'w') as f:
    f.write(str(matrix2))

matrix_add = matrix1 + matrix2
matrix_mul = matrix1 * matrix2
matrix_matmul = matrix1 @ matrix2

with open('matrix+.txt', 'w') as f:
    f.write(str(matrix_add))

with open('matrix*.txt', 'w') as f:
    f.write(str(matrix_mul))

with open('matrix@.txt', 'w') as f:
    f.write(str(matrix_matmul))
