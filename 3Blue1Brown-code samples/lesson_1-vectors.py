"""
This directory will contain python code examples of Linear Algebra ideas from "Essence of linear algebra"
by 3Blue1Brown. Here I'll implement some of Linear Algebra ideas in python code (to make it easier to understand)
for CS students. This code has no license and it's free to use, copy, paste and share!
"""

import matplotlib.pyplot as plt
import numpy as np
import random


"""
each vector can be represented as sorted sequence or as a dot on a n-dimensional scatter
Here's the code for showing different vectors on plane
It supports only 2d vectors btw

Each vectors coordinates represent "path" to the dot like:
go 5 steps right on x coord, then go 3 steps down on y coord (for vector [5 -3])

for 3 dimensional vectors it represents:
x "path", y "path", z "path" (z is upper)
"""

def build_vector_coords(vectors: list):
    colors = ['g', 'r', 'b', 'm', 'y']
    x, y = list([lst[0] for lst in vectors]), list([lst[1] for lst in vectors])
    print(x, y)
    x_min, x_max, y_min, y_max = (min(x) - 5), (max(x) + 5), (min(y) - 5), (max(y) + 5)
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))

    cols = []
    for i in range(len(x)):
        c = random.choice(colors)
        cols.append(c)
        ax.scatter(x[i], y[i], c=c)
  
    for i in range(len(x)):
        ax.plot([x[i], x[i]], [0, y[i]], c=cols[i], ls='--')
        ax.plot([0, x[i]], [y[i], y[i]], c=cols[i], ls='--')

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

    plt.show()


build_vector_coords([[4, 5], [-4, 5], [0, -1], [-5, -10]])


# but we can also sum vectors

# this code is simmilar to the upper one but:
def sum_vectors(vectors: list):
    colors = ['g', 'r', 'b', 'm', 'y']
    x, y = list([lst[0] for lst in vectors]), list([lst[1] for lst in vectors])
    print(x, y)
    x_min, x_max, y_min, y_max = (min(x) - 5), (max(x) + 5), (min(y) - 5), (max(y) + 5)
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))

    cols = []
    for i in range(len(x)):
        c = random.choice(colors)
        cols.append(c)
        ax.scatter(x[i], y[i], c=c)
  
    for i in range(len(x)):
        ax.plot([x[i], x[i]], [0, y[i]], c=cols[i], ls='--')
        ax.plot([0, x[i]], [y[i], y[i]], c=cols[i], ls='--')

    # here we draw a sum dot on our plot
    ax.scatter(sum(x), sum(y), c='red')

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

    plt.show()


sum_vectors([[1, 2], [3, -1]])


# we can also multiply vectors

def mul_vectors(vector: list, num: float):
    x, y = vector
    print(x, y)
    x_min, x_max, y_min, y_max = (x - 5), (x + 5), (y - 5), (y + 5)
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.title.set_text(f'vector {vector} multiplied by {num}')

    ax.scatter(x, y, c='g')
  
    ax.plot([x, x], [0, y], c='g', ls='--')
    ax.plot([0, x], [y, y], c='g', ls='--')

    # here we draw a sum dot on our plot
    ax.scatter(x * num, y * num, c='red')
    
    ax.plot([x * num, x * num], [0, y * num], c='r', ls='--')
    ax.plot([0, x * num], [y * num, y * num], c='r', ls='--')


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

    plt.show()


mul_vectors([1, 2], 2)