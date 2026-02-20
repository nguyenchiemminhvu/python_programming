###
#  Matplotlib is a powerful plotting library in Python that allows you to create a wide variety of static, animated, and interactive visualizations. The basic structure of a Matplotlib plot consists of three main components:
# figure -> axes -> plot elements
# 
# Figure
#  └── Axes
#        ├── XAxis
#        ├── YAxis
#        ├── Lines
#        ├── Text
#        ├── Patches
# 
# EXP: If truly understand matplotlib, every other visuallization library in python will be easy to learn.
#
# In this example below, we will create a simple line plot of speed vs time using matplotlib. We will generate a time array and a corresponding speed array, then plot them using the plot() function. We will also customize the plot by adding titles, labels, legends, and a grid for better visualization.
#
# Relationship between figure, axes, and plot elements:
# - Figure: The overall container for the plot. It can contain multiple axes.
# - Axes: The area where the data is plotted. It can contain multiple plot elements such as lines, markers, etc.
# - Plot elements: The actual data representations (e.g., lines, points) that are drawn on the axes.
#
# It is recommend to always use fig, axes = plt.subplots() to create a figure and axes, as it provides more control and flexibility over the plotting area.
# Never rely on plt.plot(...) alone, as it can lead to confusion and less control over the plot, especially when dealing with multiple plots or subplots.
# Also recommend to label every plot elements: title, x-axis, y-axis, legend, grid, units... for precise reading value in analysis.
#
#
# matplotlib has two APIs:
# 1. Object-oriented API: This is the recommended way to create plots, because that's how serious analysis is done.
# 2. Pyplot API: This is a simpler interface that is often used for quick plotting, but it can lead to less control and confusion when creating complex plots.
###

import matplotlib.pyplot as plt

# Generate data
x = [0, 1, 2, 3, 4, 5]
y1 = x[:]
y2 = [0, 1, 4, 9, 16, 25]
y3 = [0, 1, 8, 27, 64, 125]
datas = [y1, y2, y3]
# Create a figure and axes
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(6, 4), sharex=True)  # Create 3 subplots in a single column, sharing the x-axis

# Plot the data on the axes
for i, ax in enumerate(axs):
    ax.plot(x, datas[i], label=f'Line {i+1}', linestyle=['-', '--', '-.'][i], marker='o', color=f'C{i}')  # Plot each line with markers
    ax.set_title(f'Line {i+1} Plot')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True, which='major', linestyle='--', alpha=0.7, linewidth=0.7)  # Add grid to each subplot
    ax.grid(True, which='minor', linestyle=':', alpha=0.5, linewidth=0.5)  # Add minor grid for better visibility
    ax.minorticks_on()  # Enable minor ticks for better grid visibility

axs[-1].set_xlabel('x')  # Set x-axis label for the last subplot

plt.suptitle('Multiple Lines Plot')  # Set a suptitle for the entire figure
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
