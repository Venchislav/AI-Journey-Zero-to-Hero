import numpy as np

"""
We have 2 matrices as input:
A - matrix of coefficients in our linear equation
B - matrix of outputs
"""


def np_system_of_lin_equations(A, B):
    return np.dot(np.linalg.inv(A), B)


A = [[3, 2], [2, -1]]
B = [[8], [3]]

print(np_system_of_lin_equations(A, B))
