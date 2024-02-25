# This is the second part of 3Blue1Brown Essence of linear algebra series
# So let's start


# each vector can be represented through basis vectors:
# i for x and j for y
# here's a code for ploting it:

import matplotlib.pyplot as plt
import numpy as np
import random

def basis_vectors():
    
    x_min, x_max, y_min, y_max = -5, 5, -5, 5
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))

    ax.scatter(1, 0, c='r', label='i')
    ax.scatter(0, 1, c='g', label='j')

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


basis_vectors()
# as you can see nothing hard here:
# knowing this we can represent vector [5 -2] as 5i + (-2)j
# and nothing will change


# span:

# we can sum two vectors
# but we can also modify these two vectors
# we can multiply them on some scalar (we can scale them)
# so that let's us draw plenty of different unique dots (like 5i + 2j, 3i + (-1)j etc.)

# but vectors with the same direction have "limited" (actually not it's still inf) span. Their span is stored on line
# there's only one "worst" case when we don't have span. If our vectors are in the same coordinate and have the length of 0


# I think it's easier to think about it through formula:
# av + bw (v, w - vectors), (a, b - scalars)

def span_visualizer2d(vectors: list):
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
        ax.scatter(x[i], y[i], c=c, label='vector')

    # if vectors don't have the same direction
    if not (x[1] / y[1]) == (x[0] / y[0]):
        ax.title.set_text('Normal span')
        # plotting a dot on every tick of x and y
        for i in range(y_min, y_max + 1):
            for j in range(x_min, x_max + 1):
                ax.scatter(j, i, c='r', label='span')

    # if vectors have the same direction
    elif ((x[1] / y[1]) == (x[0] / y[0])) and ((x[1] - x[0] != 0) and (y[1] - y[0] != 0)):
        ax.title.set_text('Line span')
        # plotting the line representing our linear span
        x_, y_ = [-1 * sum(x), sum(x) * 10], [-1 * sum(y), sum(y) * 10]
        plt.plot(x_, y_, marker = 'o', label='span')
    
    # if vectors are null vectors (len 0)
    else:
        ax.title.set_text('Here we do not have span')
  
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
    plt.legend()
    plt.show()


span_visualizer2d([[3, 1], [6, 2]])
span_visualizer2d([[3, 1], [7, 5]])
span_visualizer2d([[2, 2], [2, 2]])
