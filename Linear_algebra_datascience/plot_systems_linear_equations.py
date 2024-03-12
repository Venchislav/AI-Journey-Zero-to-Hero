import matplotlib.pyplot as plt
import numpy as np


def basis_vectors():
    x_min, x_max, y_min, y_max = -5, 5, -5, 5
    ticks_freq = 1

    fig, ax = plt.subplots(figsize=(9, 9))

    ax.title.set_text('Equation 3a + 2b = 8')
    for i in range(10):
        ax.scatter(-1 * i, (-1.5 * i) - 3, c='g')
        ax.scatter(i, (1.5 * i) - 3, c='g')
    ax.plot([-10, 10], [-18, 12], c='g')

    ax.set(xlim=(x_min - 1, x_max + 1), ylim=(y_min - 1, y_max + 1), aspect='equal')

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    x_ticks = np.arange(x_min, x_max + 1, ticks_freq)
    y_ticks = np.arange(y_min, y_max + 1, ticks_freq)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    ax.set_xticks(np.arange(x_min, x_max + 1), minor=True)
    ax.set_yticks(np.arange(y_min, y_max + 1), minor=True)

    ax.grid(color='grey', linewidth=1, linestyle='-')
    plt.legend()
    plt.show()


basis_vectors()
