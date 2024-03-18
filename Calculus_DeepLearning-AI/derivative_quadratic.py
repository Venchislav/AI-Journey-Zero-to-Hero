import numpy as np


def parabola(x):
    return x ** 2


def slope(x0, x1):
    print(f'derivative is {2 * x0} btw')
    return (parabola(x0 + (x1 - x0)) - parabola(x0)) / (x1 - x0)  # - slope


print(slope(1, 1.5))
