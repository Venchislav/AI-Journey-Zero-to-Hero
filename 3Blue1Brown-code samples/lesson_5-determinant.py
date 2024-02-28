import numpy as np
import matplotlib.pyplot as plt


"""
okay... we stopped at space scaling. We've already discussed some things like scaling shear, flip and other
But logically, we can describe power of our changes with number. Number representing square of square with i and j sides.
Or number representing volume of parallelepiped with i, j, and k sides.

This number is called   D E T E R M I N A N T

If our space is flipped (meaning j is not at the same axis in connection to i) we can say that determinant < 0.
If our vectors are turned into null vectors or have the same direction (meaning it's line) determinant = 0


To callculate determinant for matrix [[a, b][c, d]] we should do a * d - b * c
"""

# numpy implementation


matrix = np.array([[1, 2], [3, 4]])

# 1 * 4  -  2 * 3  =  -2
det_res = np.linalg.det(matrix)

print(det_res)


# from scratch

def determinant_implementation(matrix):
    if type(matrix) == list:
        matrix = np.array(matrix)

    if matrix.shape == (2, 2):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        st = matrix[0][0] * determinant_implementation([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
        nd = matrix[0][1] * determinant_implementation([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
        rd = matrix[0][2] * determinant_implementation([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])

        return st - nd + rd


print(determinant_implementation([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 0
print(determinant_implementation([[1, 2], [3, 4]]))  # -2