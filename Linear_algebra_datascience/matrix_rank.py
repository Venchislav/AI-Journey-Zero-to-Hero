import numpy as np


def two_d_matrix_rank(matrix):
    assert isinstance(matrix, (np.ndarray))
    assert matrix.shape == (2, 2)

    if not matrix.any():
        return 'rank is 0'
    elif matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == 0:
        return 'rank is 1'
    else:
        return 'rank is 2'


matrix = np.array([[1, 2], [3, 4]])
print(two_d_matrix_rank(matrix))


matrix = np.array([[1, 2], [2, 4]])
print(two_d_matrix_rank(matrix))

matrix = np.array([[0, 0], [0, 0]])
print(two_d_matrix_rank(matrix))
