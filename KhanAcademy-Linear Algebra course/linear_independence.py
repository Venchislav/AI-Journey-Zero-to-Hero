import numpy as np
import matplotlib.pyplot as plt


"""
Lenearly dependent vectors means that vector a can be
represented as another vector b modified in some way

ex:

[2 3]   [4 6]
   same to
[2 3]  2[2 3]

To make it easier for goofy ahh brainrotted alpha kfc kids:
It means they're on the same line
(but it's not true)

There's a plot example down there:
"""


def linearly_dependent_vectors_example():
    
    x_min, x_max, y_min, y_max = -5, 5, -5, 5
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))

    ax.title.set_text('Linearly dependent vectors example')

    for i in range(-5, 5, 1):
        ax.scatter(i, i, c='g')

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


linearly_dependent_vectors_example()



def linearly_independent_vectors_example():
    
    x_min, x_max, y_min, y_max = -5, 5, -5, 5
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))

    ax.title.set_text('Linearly independent vectors example')

    for _ in range(-5, 5, 1):
        ax.scatter(np.random.randint(-5, 5), np.random.randint(-5, 5), c='g')

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


linearly_independent_vectors_example()
# p.s there's a small chance they will spawn as linearly dependent


"""
Vectors are also linearly dependent if they are represented as arithmetical sequence

[9 5]  is linearly dependent to 
[2 3] [7 2]

as [9 5] = [2 3] + [7 2]
"""