###
# Practice matplotlib about limits, ticks, coordinates
#
# Transform parameter includes:
# - ax.transData: Transform from data coordinates to display coordinates (default for plotting)
# - ax.transAxes: Transform from axes coordinates (0 to 1) to display coordinates
# - ax.transFigure: Transform from figure coordinates (0 to 1) to display coordinates
# - ax.transScale: Transform for scaling data coordinates (e.g., log scale)
# - ax.transLimits: Transform for setting limits on data coordinates
# - ax.transAffine: Transform for applying affine transformations (e.g., rotation, translation)
# - ax.transComposite: Composite transform that combines multiple transforms
# - ax.transBlend: Transform for blending between different coordinate systems
# - ax.transData.inverted(): Inverse transform from display coordinates back to data coordinates
# - ax.transAxes.inverted(): Inverse transform from display coordinates back to axes coordinates
# - ax.transFigure.inverted(): Inverse transform from display coordinates back to figure coordinates
# - ax.transScale.inverted(): Inverse transform for scaling data coordinates
# - ax.transLimits.inverted(): Inverse transform for setting limits on data coordinates
# - ax.transAffine.inverted(): Inverse transform for applying affine transformations
# - ax.transComposite.inverted(): Inverse composite transform
# - ax.transBlend.inverted(): Inverse transform for blending between different coordinate systems
###

import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 5, 100)
y = np.sin(x)

min_x, max_x = np.min(x), np.max(x)
min_y, max_y = np.min(y), np.max(y)

# Create a figure and axes
fig, ax = plt.subplots(figsize=(6, 4))

# Plot the data
ax.plot(x, y, label='y = sin(x)', color='blue', linestyle='-', linewidth=0.8)

# Set limits for x and y axes
ax.set_xlim(min_x - 0.5, max_x + 0.5)
ax.set_ylim(min_y - 0.5, max_y + 0.5)

ax.set_xlabel('x')  # Set x-axis label
ax.set_ylabel('y')  # Set y-axis label
ax.grid(True, which='both', linestyle='--', alpha=0.7, linewidth=0.7)
ax.legend()

ax.autoscale(enable=False, axis='both')  # Disable autoscaling to maintain the set limits

ax.set_xticks(np.arange(min_x, max_x + 1, 1), minor=False)  # Set x-ticks at integer values
ax.set_xticks(np.arange(min_x, max_x + 0.5, 0.25), minor=True)  # Set minor x-ticks at intervals of 0.25

ax.set_yticks(np.arange(-1, 1.5, 0.5), minor=False)  # Set y-ticks at intervals of 0.5
ax.set_yticks(np.arange(-1, 1.25, 0.25), minor=True)  # Set minor y-ticks at intervals of 0.25

ax.text(0.5, 0.5, "Center of axes", fontsize=12, color='red', transform=ax.transAxes, ha='left', va='top')
ax.text(1, 0.8415, "Data point (1, sin(1))", fontsize=10, color='green', transform=ax.transData, ha='left', va='top')

plt.suptitle('Line Plot of y = sin(x)')
plt.tight_layout(rect=(0, 0, 1, 0.95))
plt.show()
