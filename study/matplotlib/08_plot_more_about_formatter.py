###
# In this example, we will learn more about formatters in matplotlib.
#
# Formatters are used to control the appearance of tick labels on the axes.
# Major formatters:
# - NullFormatter: No labels.
# - FuncFormatter: User-defined function to format labels.
# - FormatStrFormatter: Format labels using a format string.
#
# Minor formatters:
# - NullFormatter: No labels.
# - FuncFormatter: User-defined function to format labels.
# - FormatStrFormatter: Format labels using a format string.
#
# We will see how to use these formatters to customize the tick labels on our plots.
###


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, MultipleLocator, AutoMinorLocator
from matplotlib.ticker import NullFormatter, FuncFormatter, FormatStrFormatter

# sample data
x = np.linspace(0, 10, 100)
y = np.sin(x / 2) * np.cos(x / 3)

# plotting
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(x, y, label='sin(x/2) * cos(x/3)', color='blue', linewidth=1)

ax.grid(True, which='major', linestyle='--', color='gray', alpha=0.7)
ax.grid(True, which='minor', linestyle=':', color='gray', alpha=0.5)

ax.xaxis.set_major_locator(MultipleLocator(2)) 
ax.xaxis.set_minor_locator(AutoMinorLocator(10))

ax.xaxis.set_major_formatter(FuncFormatter(lambda val, pos: f'{val:.1f} ms')) # This will format major tick labels to one decimal place
ax.yaxis.set_major_formatter(FuncFormatter(lambda val, pos: f'{val:.1f} %')) # This will format major tick labels to two decimal places

plt.suptitle('More about Locators in Matplotlib', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
