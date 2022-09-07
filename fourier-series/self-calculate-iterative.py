import numpy as np
from matplotlib import pyplot as plt


def trangular(x):
    if x < -2 or x > 2:
        return 0
    elif -2 <= x <= -1:
        return x + 2
    elif -1 <= x <= 1:
        return -1 * x
    elif 1 <= x <= 2:
        return x - 2


def square(x):
    if x < 0:
        return 1
    elif 0 <= x < 3:
        return -1
    elif x == 3:
        return 1


start = -3
end = 3
step = 0.001
x = np.arange(start, end, step)
y1 = []
y2 = []
for i in range(len(x)):
    y1.append(trangular(x[i]))

for i in range(len(x)):
    y2.append(square(x[i]))


w = 2 * np.pi / 6

for c in range(1, 11):
    a1 = []
    b1 = []
    g1 = []

    a2 = []
    b2 = []
    g2 = []
    for k in range(c + 1):
        a1.append((1 / 3) * (np.sum(y1 * np.cos(k * w * x)) * step))
        b1.append((1 / 3) * (np.sum(y1 * np.sin(k * w * x)) * step))

    for t in x:
        temp = 0
        for k in range(c + 1):
            temp += a1[k] * np.cos(k * w * t) + b1[k] * np.sin(k * w * t)
        temp += a1[0] / 2
        g1.append(temp)

    for k in range(c + 1):
        a2.append((1 / 3) * (np.sum(y2 * np.cos(k * w * x)) * step))
        b2.append((1 / 3) * (np.sum(y2 * np.sin(k * w * x)) * step))

    for t in x:
        temp = 0
        for k in range(c + 1):
            temp += a2[k] * np.cos(k * w * t) + b2[k] * np.sin(k * w * t)
        temp += a2[0] / 2
        g2.append(temp)

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x, y1, 'm')
    axs[1, 0].plot(x, y2, 'm')
    axs[0, 1].plot(x, g1)
    axs[1, 1].plot(x, g2)
    plt.show()
