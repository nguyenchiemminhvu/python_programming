###
# subplots grid
###

import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

z1 = np.tan(x)
z2 = np.exp(-x)

# Create a figure and a 2x2 grid of subplots
fix, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True)

print(axs.shape)  # (2, 2)

# Plot on the first column
axs[0, 0].plot(x, y1, label='sin(x)', color='blue')
axs[1, 0].plot(x, y2, label='cos(x)', color='orange')

# Plot on the second column
axs[0, 1].plot(x, z1, label='tan(x)', color='green')
axs[1, 1].plot(x, z2, label='exp(-x)', color='red')

# Set titles and labels
axs[0, 0].set_title('Sine Function')
axs[1, 0].set_title('Cosine Function')
axs[0, 1].set_title('Tangent Function')
axs[1, 1].set_title('Exponential Decay')

for ax in axs.flat:
    ax.set_ylabel('y')
    ax.legend()
    ax.grid()

# Adjust layout
plt.tight_layout()
plt.show()
