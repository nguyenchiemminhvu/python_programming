###
# In this example, we will create a template for plotting time series data using matplotlib.
# This template can be reused for different time series datasets by simply changing the data and labels.
###

import numpy as np
import matplotlib.pyplot as plt

# sample time series data
x = np.linspace(0, 10, 100)
row_data = [
    np.sin(x) + np.random.normal(0, 0.1, size=x.shape),
    np.cos(x) + np.random.normal(0, 0.1, size=x.shape),
    np.sin(x) * np.cos(x) + np.random.normal(0, 0.1, size=x.shape)
]

# ploting
fig, axs = plt.subplots(nrows=len(row_data), ncols=1, figsize=(12, 7), sharex=True)

for i, (ax, row) in enumerate(zip(axs, row_data)):
    ax.plot(x, row, label=f'Series {i+1}')
    ax.set_ylabel('Value', fontsize=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.legend(loc='upper right')

axs[-1].set_xlabel('Time', fontsize=12)
fig.align_ylabels()  # align y labels if there are multiple subplots

plt.suptitle('Time Series Plot Template', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # adjust layout to make room for suptitle
plt.show()
