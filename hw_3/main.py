from matrix import Matrix
from mixin_matrix import MixinMatrix
import numpy as np

def easyTask():
    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))
    f_sum = open('artifacts/easy/matrix+.txt', 'w')
    f_mul = open('artifacts/easy/matrix_mul.txt', 'w')
    f_matmul = open('artifacts/easy/matrix@.txt', 'w')
    c = a + b
    f_sum.write(c.__str__())
    c = a * b
    f_mul.write(c.__str__())
    c = a @ b
    f_matmul.write(c.__str__())

def mediumTask():
    a = MixinMatrix(np.random.randint(0, 10, (10, 10)))
    b = MixinMatrix(np.random.randint(0, 10, (10, 10)))
    (a + b).__toFile__("artifacts/medium/matrix+.txt")
    (a * b).__toFile__("artifacts/medium/matrix_mul.txt")
    (a @ b).__toFile__("artifacts/medium/matrix@.txt")

if __name__ == '__main__':
    easyTask()
    mediumTask()
