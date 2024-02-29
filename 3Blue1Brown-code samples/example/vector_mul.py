import numpy as np

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


def multiply(v, G):
    result = []
    for i in range(len(G[0])):
        total = 0
        for j in range(len(v)):
            total += v[j] * G[j][i]
        result.append(total)
    return result

print(multiply([1, 2, 3], matrix_b))