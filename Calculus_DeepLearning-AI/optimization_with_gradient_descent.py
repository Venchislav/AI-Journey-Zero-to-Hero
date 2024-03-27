"""
Today I'll implement optimization of function argument (one variable)
with gradient descent. Lesss goooo
"""
from scipy.misc import derivative

def function_1(x):
    return x ** 2


def optimization_for_f1(function):
    x = 5
    slope = derivative(function, x)
    alpha = 0.0001
    while slope != 0:
        x -= alpha * slope
        slope = derivative(function, x)
    return f'argument - {x}'

print(optimization_for_f1(function_1))

print(function_1(5.5508596546555514e-17))  # it's 0
