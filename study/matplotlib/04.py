###
# Practices about mutiple axes and twin axes
#
# When having multiple y data series with different scales, units, or ranges, using twin axes can help visualize them together without confusion.
###

import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)  # First data series
y2 = np.cos(x) * 100  # Second data series with different scale

# Create a figure and axes
fig, origin_ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))

lines = []

# Plot the data on the first axes
line = origin_ax.plot(x, y1, label='y = sin(x)', color='blue', linestyle='-', linewidth=0.8)
lines.extend(line)
origin_ax.set_xlabel('x')  # Set x-axis label
origin_ax.set_ylabel('y1 (sin(x))')  # Set y-axis label for the first data series
origin_ax.grid(True, which='both', linestyle='--', alpha=0.7, linewidth=0.7)

twin_ax = origin_ax.twinx()  # Create a twin axes sharing the same x-axis
line = twin_ax.plot(x, y2, label='y = cos(x) * 100', color='orange', linestyle='-', linewidth=0.8)
lines.extend(line)
twin_ax.set_ylabel('y2 (cos(x) * 100)')  # Set y-axis label for the second data series
twin_ax.grid(False)  # Disable grid for the twin axes to avoid cluttering the plot

origin_ax.legend(handles=lines, labels=[line.get_label() for line in lines], loc='upper right')  # Legend for the first data series

plt.suptitle('Line Plot of y = sin(x) and y = cos(x) * 100 with Twin Axes')
plt.tight_layout(rect=(0, 0, 1, 0.95))
plt.show()
