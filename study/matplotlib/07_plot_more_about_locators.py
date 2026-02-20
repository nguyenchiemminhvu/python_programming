###
# In this example, we will learn more about locators in matplotlib.
#
# Locators are used to determine the position of ticks on the axes.
# Major locators:
# - NullLocator: No ticks.
# - MultipleLocator: Ticks at multiples of a base.
# 
# Minor locators:
# - AutoMinorLocator: Automatically chooses minor tick locations.
# - MultipleLocator: Ticks at multiples of a base.
#
# We will see how to use these locators to customize the ticks on our plots.
###

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, MultipleLocator, AutoMinorLocator

# sample data
x = np.linspace(0, 10, 100)
y = np.sin(x / 2) * np.cos(x / 3)

# plotting
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(x, y, label='sin(x/2) * cos(x/3)', color='blue', linewidth=1)

ax.grid(True, which='major', linestyle='--', color='gray', alpha=0.7)
ax.grid(True, which='minor', linestyle=':', color='gray', alpha=0.5)

# Setting major locators
ax.xaxis.set_major_locator(NullLocator()) # This will remove all major ticks from the x-axis
ax.xaxis.set_major_locator(MultipleLocator(2)) # This will set major ticks at every 2 units on the x-axis

# Setting minor locators
ax.xaxis.set_minor_locator(MultipleLocator(0.1)) # This will set minor ticks at every 0.1 units on the x-axis
ax.xaxis.set_minor_locator(AutoMinorLocator(10)) # This will automatically set 10 minor ticks between each major tick

plt.suptitle('More about Locators in Matplotlib', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
