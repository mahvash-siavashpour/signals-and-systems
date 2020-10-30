from matplotlib import pyplot as plt
import numpy as np

x1 = np.linspace(-20, 20, 40)

y1 = np.heaviside(x1, 1) - np.heaviside(x1 - 3, 1) + np.heaviside(x1 - 5, 1)
y21 = 2 * np.cos(2 * np.pi * x1)
y22 = 2 * np.cos(2 * 2 * np.pi * x1)
y23 = 2 * np.cos(2 * 3 * np.pi * x1)
y31 = 2 * np.cos(2 * x1)
y32 = 2 * np.cos(2 * 2 * x1)
y33 = 2 * np.cos(2 * 3 * x1)
fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4)

ax1.scatter(x1, y1, color='red', label='y -> non-periodic')
ax2.scatter(x1, y21, color='blue', label='y21 -> periodic')
ax3.scatter(x1, y22, color='blue', label='y22 -> periodic')
ax4.scatter(x1, y23, color='blue', label='y23 -> periodic')
ax5.scatter(x1, y31, color='green', label='y31 -> periodic')
ax6.scatter(x1, y32, color='green', label='y32 -> periodic')
ax7.scatter(x1, y33, color='green', label='y33 -> periodic')
fig.legend(loc='upper left')

print("y1 -> non-periodic")
print("y2 -> periodic")
print("y3 -> periodic")
plt.show()