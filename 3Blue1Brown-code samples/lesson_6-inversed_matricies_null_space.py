"""
It's pretty a lot to explain here, so let's start

To make it easier and to understand what's going on (and touch few other concepts additionaly)
Grant decided to explain it through systems of equations.

We can represent them through matrix of coefficients. Like that:

3x + 1y + 4z = 1    [3 1 4][x]   [1]
5x + 9y + 2z = 6    [5 9 2][y] = [6]
5x + 3y + 5z = 8    [5 3 5][z]   [8]

where matrix - A; vars vector - x; output - v;

Representing it in geometry we get the following thing:

Ax = v

A is some kind of transformation, and we should find x vector
that it will turn into v vector after transformation
"""

# it's really easy to inverse matrix A (inverse operation) with np

import numpy as np

matrix = np.array([[1, 2], [3, 4]])

inversed_matrix = np.linalg.inv(matrix)

print(matrix, inversed_matrix)


# visualize

import matplotlib.pyplot as plt

def plot_transformations(A, rev_A):
    
    x_min, x_max, y_min, y_max = -5, 5, -5, 5
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.title.set_text('i ans j transformed by A')
    ax.scatter(A.dot(np.array([1, 0]))[0], A.dot(np.array([1, 0]))[1], c='r', label='i')
    ax.scatter(A.dot(np.array([0, 1]))[0], A.dot(np.array([0, 1]))[1], c='g', label='j')

    ax.set(xlim=(x_min-1, x_max+1), ylim=(y_min-1, y_max+1), aspect='equal')

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    x_ticks = np.arange(x_min, x_max + 1, ticks_freq)
    y_ticks = np.arange(y_min, y_max + 1, ticks_freq)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    ax.set_xticks(np.arange(x_min, x_max+1), minor=True)
    ax.set_yticks(np.arange(y_min, y_max+1), minor=True)

    ax.grid(color='grey', linewidth=1, linestyle='-')
    plt.legend()
    plt.show()

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.title.set_text('i and j transformed by A^-1')
    transformed_i = A.dot(np.array([1, 0]))
    transformed_j = A.dot(np.array([0, 1]))
    # it's back on start position!
    ax.scatter(rev_A.dot(transformed_i)[0], rev_A.dot(transformed_i)[1], c='r', label='i')
    ax.scatter(rev_A.dot(transformed_j)[0], rev_A.dot(transformed_j)[1], c='g', label='j')

    ax.set(xlim=(x_min-1, x_max+1), ylim=(y_min-1, y_max+1), aspect='equal')

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    x_ticks = np.arange(x_min, x_max + 1, ticks_freq)
    y_ticks = np.arange(y_min, y_max + 1, ticks_freq)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    ax.set_xticks(np.arange(x_min, x_max+1), minor=True)
    ax.set_yticks(np.arange(y_min, y_max+1), minor=True)

    ax.grid(color='grey', linewidth=1, linestyle='-')
    plt.legend()
    plt.show()

plot_transformations(matrix, inversed_matrix)

# Null space:
"""
Null space is formed from vectors that turn into null vector after transformation
[0; 0]

For now it's just theory. Code will be here later.
"""