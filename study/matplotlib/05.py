###
# Practices about multiple axes to replace the limitation of twin axes
###

import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)  # First data series
y2 = np.cos(x) * 100  # Second data series with different scale
y3 = np.tan(x) * 10  # Third data series with different scale

y_data = [y1, y2, y3]
min_y = min(np.min(y) for y in y_data)
max_y = max(np.max(y) for y in y_data)

# Create a figure and axes
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(12, 2 * len(y_data)), sharex=True)

# Plot the first data series on the first axes
for i, ax in enumerate(axs):
    ax.plot(x, y_data[i], label=f'y{i + 1}', color=f"C{i}", linestyle='-', linewidth=0.8)
    ax.set_ylabel(f'y{i + 1}')  # Set y-axis label for each data series
    ax.grid(True, which='both', linestyle='--', alpha=0.7, linewidth=0.7)
    ax.legend(loc='upper right')

axs[-1].set_xlabel('x')  # Set x-axis label for the last axes

plt.suptitle('Line Plots of Multiple Data Series with Separate Axes')
plt.tight_layout(rect=(0, 0, 1, 0.95))
plt.show()
