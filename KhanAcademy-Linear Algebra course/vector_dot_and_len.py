"""
In reflect we know that we can:

Scale vectors (multiply vector by number (scalar))
Add vectors (vector of zipped elements summed up)

But can we multiply vector by vector?
Of course, we can:

It's two ways to do it:
dot product and cross product.
Here I'll show dot product:
"""

import numpy as np


def dot_product_vectors(a, b: [list, list]) -> float:
    assert len(a) == len(b)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


a = [1, 2, 3]
b = [-2, 0, 5]

print(dot_product_vectors(a, b))  # 13

# via numpy

print(np.dot(a, b))  # 13


# ---- vector length ----

# it's not just a len func. It's a formula bitch
# ||a|| = sqrt(a1^2 + a2^2 + a3^2 + ... an^2)


def get_length(vector: list) -> float:
    total = 0

    for element in vector:
        total += element ** 2

    return total ** 0.5


print(get_length(a))  # 3.7416573867739413

# fun thing that it's literally Pythagorean theorem
# Just try to draw it on a coordinate plane:

"""
|     >
|    /|
|   / |  
|  /  |  4
| /   |
|/    |
----------------------
    3
v = sqrt(4^2 + 3^2) = 5
||v|| = 5
"""
