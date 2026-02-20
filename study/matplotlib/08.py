###
# Export figure to file
#
# By using plt.savefig(), we can save the current figure to a file in various formats (e.g., PNG, PDF, SVG). This is useful for sharing or embedding the figure in documents.
###

import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and plot the data
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label='sin(x)', color='blue')
ax.set_title('Sine Function')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid()

plt.show()

# Save the figure to a file
plt.savefig('08.png', dpi=300)  # Save as PNG with high resolution