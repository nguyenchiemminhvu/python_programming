###
# Through this example, we will explore more about axes in matplotlib, including how to customize the appearance of axes, how to set limits and ticks, and how to add labels and legends.
#
# Wrong thoughts: matplotlib is about plt.plot() only.
#
# In fact, matplotlib is about manipulating the Axes objects, and everything lives inside the Axes.
#
# ax.set_xlim()
# ax.set_ylim()
# ax.set_xticks()
# ax.set_yticks()
# ax.set_xlabel()
# ax.set_ylabel()
# ax.set_facecolor()
# ax.legend()
# ax.grid()
# ax.tick_params()
# ax.spines
# ax.text()
# ax.annotate()
#
# Exp: If mastering the Axes, then mastering matplotlib.
###

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# sample data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)

# create figure and axes
fig, ax = plt.subplots(figsize=(10, 4))
fig.align_ylabels()  # align y labels if there are multiple subplots

# plot data
ax.plot(x, y, label='Noisy Sine Wave')

# config spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_color('blue')
ax.spines['bottom'].set_linewidth(1)

# config ticks
# ax.set_xticks([]) # remove x ticks
# major_ticks = [i for i in range(0, int(x[-1]) + 1, 2)] # 0, 2, 4, 6, 8, 10
# minor_ticks = [i for i in range(1, int(x[-1]) + 1, 2)] # 1, 3, 5, 7, 9
# ax.set_xticks(major_ticks, minor=False)
# ax.set_xticks(minor_ticks, minor=True)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator(5)) # how many minor ticks between 2 major ticks
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5)) # how many minor ticks between 2 major ticks
ax.tick_params(axis='x', which='major', length=10, width=1, color='blue')
ax.tick_params(axis='x', which='minor', length=5, width=1, color='gray')

# limits
ax.set_xlim(int(x[0]), int(x[-1]) + 1)
ax.set_ylim(-1.5, 1.5)

# grid
ax.grid(True, which='major', linestyle='--', linewidth=0.7, alpha=0.7)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

plt.suptitle('Customizing Axes in Matplotlib', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # adjust layout to make room for suptitle
plt.show()
