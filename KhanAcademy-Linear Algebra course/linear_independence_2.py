# vectors are linearly dependent if a * v1 + b * v2 + c * v3 = 0 (and at least one of the a, b, c != 0)
# also we can do it with det like this:

# only for 2D
def are_linearly_dep(v1, v2):
    matrix = [v1, v2]
    # if determinant == 0
    if matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == 0:
        return 'Linearly dependent!'
    else:
        return 'Linearly independent!'


a = [8, 2]
b = [16, 4]
c = [5, 2]

print(are_linearly_dep(a, b))  # Linearly dependent!
print(are_linearly_dep(a, c))  # Linearly independent!
