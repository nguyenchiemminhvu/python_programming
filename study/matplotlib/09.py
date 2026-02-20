###
# Study about scatter plot in matplotlib.
#
# ax.scatter(x, y, s=None, c=None, marker=None, alpha=None)
# x: x coordinates of the points.
# y: y coordinates of the points.
# s: size of the points.
# c: color of the points.
# marker: shape of the points.
# alpha: transparency of the points.
# Returns a PathCollection object.
#
# What is path collection?
# A PathCollection is a collection of paths that can be drawn on a plot. It is used to create scatter plots, where each point is represented as a path. The PathCollection object allows you to customize the appearance of the points, such as their size, color, shape, and transparency. You can also use it to create other types of plots, such as line plots and bar plots, by specifying the appropriate path for each point. The PathCollection object is a powerful tool for creating complex and visually appealing plots in matplotlib.
#
# Way to exampine the path collection object:
# 1. Create a scatter plot using ax.scatter() and store the returned PathCollection object in a variable.
# 2. Use the variable to access the properties of the PathCollection object, such as its size, color, marker, and alpha.
# 3. Use the properties to customize the appearance of the points in the scatter plot, such as changing their size, color, shape, and transparency.
# Example:
# x = np.random.rand(10)
# y = np.random.rand(10)
# scatter = ax.scatter(x, y, s=100, c='red', marker='o', alpha=0.5)
# print(len(scatter.get_offsets())) # Get the number of points in the scatter plot
# print(scatter.get_sizes()) # Get the size of the points
# print(scatter.get_facecolors()) # Get the color of the points
# print(scatter.get_marker()) # Get the shape of the points
# print(scatter.get_alpha()) # Get the transparency of the points
#
# scatter.set_sizes([200]) # Change the size of the points to 200
# scatter.set_facecolors(['blue']) # Change the color of the points to blue
# scatter.set_marker('x') # Change the shape of the points to 'x'
# scatter.set_alpha(0.8) # Change the transparency of the points to 0.8
###

import numpy as np
import matplotlib.pyplot as plt

# Generate some data
np.random.seed(0)
n = 50
scale = 100
locations = [(np.random.rand() * scale, np.random.rand() * scale) for i in range(n)]
masses = np.random.rand(n) * scale

# Create a scatter plot
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(
    [loc[0] for loc in locations],
    [loc[1] for loc in locations],
    s=masses,
    c=masses,
    cmap='viridis',
    alpha=0.6
)

# Insight the PathCollection object
print(f'Number of points: {len(scatter.get_offsets())}')
print(f'Sizes of points: {scatter.get_sizes()}')
print(f'Colors of points: {scatter.get_facecolors()}')
print(f'Transparency: {scatter.get_alpha()}')

# Hide the small points < 30
sizes = [s if s >= 30 else 0 for s in scatter.get_sizes()]
scatter.set_sizes(sizes)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

fig.colorbar(scatter, label='Mass')
fig.suptitle('Scatter Plot with PathCollection')
plt.show()
