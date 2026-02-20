###
# Subplots and grid spec
#
# GridSpec allows for more flexible subplot layouts.
# 
# In this example, we create a 2x2 grid where the first row spans both columns, and the second row contains two separate subplots. We also customize the grid lines for better visibility.
###

import numpy as np
import matplotlib.pyplot as plt

# Generate some data
xtop = np.linspace(0, 10, 100)
xbot = np.linspace(0, 5, 100)

ytop = np.sin(xtop)
yleft = np.cos(xbot)
yright = np.exp(-xbot)

# Create a figure and a grid of subplots
fig = plt.figure(figsize=(10, 8))

# Using grid spec to create a 2x2 layout
gs = fig.add_gridspec(2, 2)

ax_first_row = fig.add_subplot(gs[0, :])  # First row spans both columns
ax_first_row.plot(xtop, ytop, label='sin(x)', color='blue')
ax_first_row.set_title('Sine Function')
ax_first_row.legend()
ax_first_row.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax_second_row_left = fig.add_subplot(gs[1, 0])
ax_second_row_left.plot(xbot, yleft, label='cos(x)', color='orange')
ax_second_row_left.set_title('Cosine Function')
ax_second_row_left.legend()
ax_second_row_left.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax_second_row_right = fig.add_subplot(gs[1, 1])
ax_second_row_right.plot(xbot, yright, label='exp(-x)', color='red')
ax_second_row_right.set_title('Exponential Decay')
ax_second_row_right.legend()
ax_second_row_right.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

fig.suptitle('Subplots with GridSpec', fontsize=16)  # Overall title for the figure
fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for the title
plt.show()
