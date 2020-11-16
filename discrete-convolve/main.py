from matplotlib import pyplot as plt
import numpy as np


def des_convolve(X, H):
    x, h = X.copy(), H.copy()
    if len(h) > len(x):
        x, h = h, x
    if len(x) == 0:
        raise ValueError('x cannot be empty')
    if len(h) == 0:
        raise ValueError('h cannot be empty')

    h = h[::-1]
    convolved = []
    for i in range(len(x) + len(h) - 1):
        convolved.append(0)
    index = 0
    for n in range(len(convolved)):

        if n >= len(x):
            for k in range(len(x) - 1, index, -1):
                convolved[n] += x[k] * h[len(h) - 1 - index - 1 - (len(x) - 1 - k)]
            index += 1

        else:
            for k in range(n):
                convolved[n] += x[k] * h[len(h) - 1 - n + k]

    return convolved


def f(x):
    if x == 0 or x == 1 or x == 2 or x == 5 or x == 6 or x == 7:
        return 1
    else:
        return 0


x1 = np.linspace(-10, 10, 200)
xx1 = np.linspace(-20, 20, 400 - 1)

x2 = np.around(np.arange(-5, 10, 1), 2)
xx2 = np.around(np.arange(-9, 20, 1), 2)
y1 = (1 / 2) * np.exp(-2 * x1) * np.heaviside(x1, 1)
h1 = np.heaviside(x1, 1) - np.heaviside(x1 - 5, 1)

y2 = ((1 / 3) ** (-1 * x2)) * np.heaviside(-1 * x2 - 1, 1)
h2 = np.heaviside(x2 - 1, 1)

y3 = []
for i in range(len(x2)):
    y3.append(f(x2[i]))

h3 = ((1 / 3) ** x2) * np.heaviside(x2, 1)

conv1 = des_convolve(y1, h1)
conv2 = des_convolve(y2, h2)
conv3 = des_convolve(y3, h3)

# plots all functions and their convolved
fig, axs = plt.subplots(3, 3)
axs[0, 0].plot(x1, y1, color='red', label='1')
axs[0, 1].plot(x1, h1, color='red')
axs[0, 2].plot(xx1, conv1, color='red')
axs[0, 2].set_title('convolved')

axs[1, 0].stem(x2, y2, label='2')
axs[1, 1].stem(x2, h2)
axs[1, 2].stem(xx2, conv2)
axs[1, 2].set_title('convolved')

axs[2, 0].stem(x2, y3, label='3')
axs[2, 1].stem(x2, h3)
axs[2, 2].stem(xx2, conv3)
axs[2, 2].set_title('convolved')

fig.legend(loc='upper left')
plt.subplots_adjust(hspace=1)


# plots only the convolved results
fig, axs = plt.subplots(3, 1)
axs[0].plot(xx1, conv1, color='red')
axs[1].stem(xx2, conv2)
axs[2].stem(xx2, conv3)
plt.show()
