import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return x ** 2


def derivative(y):
    return 2 * y


values = np.arange(-100, 100)
y_values = np.array(list(map(lambda x: function(x), values)))

cur_pos = (80, function(80))
lr = 0.001

for _ in range(1000):
    new_x = cur_pos[0] - lr * derivative(cur_pos[0])
    new_y = function(new_x)
    plt.plot(values, y_values)
    plt.scatter(cur_pos[0], cur_pos[1], c='r')
    plt.pause(0.001)
    plt.clf()
