import array


class MatrixAddException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"MatrixAddException: {self.message}."


class MatrixMulException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"MatrixMulException: {self.message}."


class Matrix:
    def __init__(self, mat):
        self.matrix = mat
        self.n = len(mat)
        self.m = len(mat[0])

    def __add__(self, other):
        if self.n == other.n and self.m == other.m:
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.m)] for i in range(self.n)])
        else:
            raise MatrixAddException("not equal dimens matrixes")

    def __matmul__(self, other):
        if self.m == other.n:
            return Matrix([[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.m)])
                            for j in range(other.m)]
                           for i in range(self.n)])
        else:
            raise MatrixMulException("not appropriate dimens matrixes")

    def __mul__(self, other):
        if self.m == other.m and self.n == other.n:
            return Matrix([[self.matrix[i][j] * other.matrix[i][j]
                            for j in range(other.m)]
                           for i in range(self.n)])
        else:
            raise MatrixMulException("not appropriate dimens matrixes")

    def __str__(self):
        result = ""
        for i in range(self.n):
            for j in range(self.m):
                result += f"{self.matrix[i][j]} "
            result += '\n'
        return result
