###
# Get familiar with Bar plot.
#
# Used for:
# - Comparing categorical data.
# - Showing trends over time (with grouped bars).
#
# ax.bar(x, height, width=0.8, bottom=None, align='center', color=None, edgecolor=None, linewidth=None, label=None, **kwargs)
#
# Key parameters:
# - x: The categories or positions of the bars.
# - height: The heights of the bars.
# - width: The width of the bars (default is 0.8).
# - bottom: The y-coordinate of the bars' bases (default is 0).
# - align: The alignment of the bars ('center' or 'edge').
# - color: The color of the bars.
# - edgecolor: The color of the bar edges.
# - linewidth: The width of the bar edges.
# - label: The label for the bars (used in legends).
###

import numpy as np
import matplotlib.pyplot as plt

# Sample data
keys = ['A', 'B', 'C', 'D', 'E']
freq = [10, 15, 7, 12, 20]

# Create a bar plot
fig = plt.figure(figsize=(8, 6))

gs = fig.add_gridspec(2, 1)
ver = fig.add_subplot(gs[0, 0])
hor = fig.add_subplot(gs[1, 0])

containers = ver.bar(keys, freq, color='skyblue', edgecolor='black', linewidth=1.5, label='Frequency')

for container in containers:
    container.set_color('lightcoral')  # Change the color of each bar
    container.set_edgecolor('black')  # Set edge color for each bar
    container.set_linewidth(2)  # Set edge linewidth for each bar

ver.set_xlabel('Categories')
ver.set_ylabel('Frequency')

containers = hor.barh(keys, freq, color='lightgreen', edgecolor='black', linewidth=1.5, label='Frequency')

hor.set_xlabel('Frequency')
hor.set_ylabel('Categories')

fig.suptitle('Bar Plot Example', fontsize=16)
fig.tight_layout(pad=3.0)
plt.show()
