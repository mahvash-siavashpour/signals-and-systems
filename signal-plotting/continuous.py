from matplotlib import pyplot as plt
import numpy as np


def f(x):
    if x > 1:
        return np.exp(-1 * x) * (np.sin(x) + np.cos(x)) * np.heaviside(x, 1)
    elif -1 <= x <= 1:
        return 1
    elif x < -1:
        return 0


x1 = np.linspace(-3, 3, 6000)
y1 = np.exp(-3 * x1)
y2 = np.exp(-3 * x1) * np.heaviside(x1, 1)
y3 = np.exp(-3 * x1) * np.heaviside(x1, 1) + 2 * np.sin(x1 + 2)
y4 =[]
for i in range(len(x1)):
   y4.append(f(x1[i]))


fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x1, y1, color='red', label='y=e^-3x')
axs[0, 1].plot(x1, y2, color='blue', label='y=e^-3x u')
axs[1, 0].plot(x1, y3, color='green', label='y=e^-3x u + 2sin(x+2)')
axs[1, 1].plot(x1, y4, color='black', label='y=piece-wise')

fig.legend(loc='upper left')

plt.show()