import numpy as np


vector_1 = np.array([1, 2, 3])
vector_2 = np.array([3, 4, 5])

# this is crossproduct
print(np.cross(vector_1, vector_2))



vector_1 = np.array([1, 2])
vector_2 = np.array([3, 4])

# this is crossproduct for 2x2
print(np.cross(vector_1, vector_2))
# but representing vectors on paper we can draw parallelogram
# it's square will be our crossproduct
# it equals vector_1 * vector_2. Let's use determinant (it will be explained later) and boom. -2, here's the result


# but what do we do with 3dims
# I don't know...
# okay, there's an illustration for lesson 8 in illustrations folder
# but it will be explained in 9th chapter

# 9th chapter's here

# I watched it

# and didn't understand anything (with this intuition)
# so I hope I'll understand it from khan academy course

# bruh


def cross_product(v, w):
    assert np.array(v).shape == np.array(w).shape

    return v[0] * w[1] - v[1] * w[0]


print(cross_product(vector_1, vector_2))