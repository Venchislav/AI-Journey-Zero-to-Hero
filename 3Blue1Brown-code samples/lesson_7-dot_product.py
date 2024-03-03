import numpy as np

vector_1 = np.array([1, 2, 3])
vector_2 = np.array([4, 5, 6])

print(np.dot(vector_1, vector_2))  # 32
print(vector_1.dot(vector_2))  # also 32

# meaning 1 * 4 + 2 * 5 + 3 * 6

# implement from scratch

vector_1 =[1, 2, 3]
vector_2 = [4, 5, 6]


def dot_product(v, v1):
    if np.array(v).shape != np.array(v1).shape:
        raise ValueError
    
    connected = tuple(zip(v, v1))
    
    res = []
    for i in range(len(v)):
        res.append(connected[i][0] * connected[i][1])
    

    return sum(res)

print(dot_product(vector_1, vector_2))

