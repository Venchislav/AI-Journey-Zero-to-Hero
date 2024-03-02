# simple implementation of Gauss Elimination on python

# Gauss Elimination represents equation as a matrix of coeffs
# Then it applies mathematical methods and gives us output


import numpy as np


unknown = int(input('Number of unknown variables: '))

# we have additional column for our result
matrix = np.zeros((unknown, unknown + 1))
print(matrix)

# output vector
output = np.zeros(unknown)

for i in range(unknown):
    for j in range(unknown + 1):
        matrix[i][j] = float(input(f'Input coeffitient [{i}, {j}] value: '))


for i in range(unknown):
    if matrix[i][i] == 0.0:
        raise ZeroDivisionError
    
    for j in range(i + 1, unknown):
        ratio = matrix[j][i] / matrix[i][i]

        for k in range(unknown + 1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

output[unknown-1] = matrix[unknown-1][unknown] / matrix[unknown-1][unknown-1]

for i in range(unknown-2, -1, -1):
    output[i] = matrix[i][unknown]

    for j in range(i+1, unknown):
        output[i] = output[i] - matrix[i][j] * output[j]
    output[i] = output[i] / matrix[i][i]

for i in range(unknown):
    print(f'{i} - {output[i]}')
    

    
