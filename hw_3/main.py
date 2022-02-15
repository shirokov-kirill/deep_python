from matrix import Matrix
import numpy as np

if __name__ == '__main__':
    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))
    f_sum = open('artifacts_easy/matrix+.txt', 'w')
    f_mul = open('artifacts_easy/matrix_mul.txt', 'w')
    f_matmul = open('artifacts_easy/matrix@.txt', 'w')
    c = a + a
    f_sum.write(c.__str__())
    c = a * a
    f_mul.write(c.__str__())
    c = a @ a
    f_matmul.write(c.__str__())
