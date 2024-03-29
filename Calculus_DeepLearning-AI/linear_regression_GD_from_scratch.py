import pandas as pd
import matplotlib.pyplot as plt


def optimize(m, b, data, lr, epochs):
    n = data.shape[0]
    dldm = 0
    dldb = 0
    for epoch in range(epochs):
        for i in range(n):
            x = data.iloc[i]['TV']
            y = data.iloc[i]['Sales']

            # calculate gradients:

            dldm += -2 * x * (y - (m * x + b))
            dldb += 2 * (y - (m * x + b))
            print(dldm, dldb)
            break

        m = m - (dldm / n * lr)
        b = b - (dldb / n * lr)

    return m, b


df = pd.read_csv('E:/CODING/DATASETS/TV/tvmarketing.csv')


lr = 0.0001
m, b = 0, 0
m, b = optimize(m, b, df, lr, 1000)

print(m * df.iloc[0]['TV'] + b)
print(df.iloc[0]['Sales'])

plt.scatter(df['TV'], df['Sales'])
plt.plot(list(range(0, 300)), [m * x + b for x in range(0, 300)], color='red')
plt.show()
