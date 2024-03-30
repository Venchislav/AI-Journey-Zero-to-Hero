import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


def loss_func(m, b, data, y):
    err = 0
    for x, y_ in zip(data, y):
        err += (m * x + b - y_) ** 2
    return err / len(data)


def optimize(m, b, X, y, lr, epochs):
    n = len(X)
    dldm = 0
    dldb = 0
    for epoch in range(epochs):
        for i in range(n):
            xi = X[i]
            yi = y[i]

            # calculate gradients:

            dldm += -2 * xi * (yi - (m * xi + b))
            dldb += 2 * (yi - (m * xi + b))

        m = m - (dldm / n * lr)
        b = b - (dldb / n * lr)
        print(loss_func(m, b, X, y))

    return m, b


X = []
y = []
for i in range(10_000):
    a = random.uniform(1.0, 300.0)
    X.append(a)
    y.append(a * 5 + random.randint(-15, +15))

lr = 0.0001
m, b = 0, 0
m, b = optimize(m, b, X, y, lr, 1000)

plt.scatter(X, y)
plt.plot(list(range(0, 300)), [m * x + b for x in range(0, 300)], color='red')
plt.show()
