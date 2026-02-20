###
# ax.plot() actually returns a list of line objects, its properties can be modified after plotting.
###

import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

y_data = [y1, y2, y3]
y_lines = []  # List to store line objects for later modification

# Create a figure and axes
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))

# Plot the data
for i, y in enumerate(y_data):
    line = ax.plot(x, y, label=f'Line {i+1}', linestyle=['-', '--', '-.'][i], marker=['o', 's', '^'][i], color=f'C{i}', linewidth=0.8, markersize=3)[0]
    y_lines.append(line)  # Store the line object for later modification

    line.set_alpha(np.random.rand())  # Set random transparency for each line
    line.set_zorder(i)  # Set z-order to control which line is on top

ax.grid(True, which='major', linestyle='--', alpha=0.7, linewidth=0.7)  # Add grid to the plot
ax.grid(True, which='minor', linestyle=':', alpha=0.5, linewidth=0.5)  # Add minor grid for better visibility
ax.minorticks_on()
ax.legend()

plt.show()