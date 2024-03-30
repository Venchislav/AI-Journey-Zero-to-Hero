import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('E:\CODING\DATASETS\TV\data.csv')

X = df.iloc[:, 0]
Y = df.iloc[:, 1]

m = 0
c = 0

L = 0.0001
epochs = 1000

n = float(len(X))


for i in range(epochs):
    Y_pred = m * X + c
    D_m = (-2 / n) * sum(X * (Y - Y_pred))
    D_c = (-2 / n) * sum(Y - Y_pred)
    m = m - L * D_m
    c = c - L * D_c

print(m, c)


plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
plt.show()
