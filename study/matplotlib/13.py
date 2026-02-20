###
# Histogram - choosing bins
#
# Choosing the right number of bins is crucial for accurately representing the data distribution. Too few bins can oversimplify the data, while too many bins can create a noisy histogram that obscures the underlying patterns.
#
# There are several methods for determining the optimal number of bins:
# 1. Sturges' Rule: bins = ceil(log2(n) + 1), where n is the number of data points.
# 2. Freedman-Diaconis Rule: bins = ceil((max(data) - min(data)) / (2 * IQR(data) / n^(1/3))), where IQR is the interquartile range. Where IQR = Q3 - Q1, Q1 is the 25th percentile and Q3 is the 75th percentile of the data.
# 3. Square-root Choice: bins = ceil(sqrt(n)).
#
# In practice, it's often helpful to experiment with different bin sizes and visually inspect the resulting histograms to find the one that best represents the data distribution.
#
# built-in bins options:
# - 'auto': Automatically determine the optimal number of bins using a combination of the above methods.
# - 'sturges': Use Sturges' rule to determine the number of bins.
# - 'fd': Use the Freedman-Diaconis rule to determine the number of bins.
# - 'sqrt': Use the square-root choice to determine the number of bins.
#
# Example:
# ax.hist(x, bins='auto')
# ax.hist(x, bins='sturges')
# ax.hist(x, bins='fd')
# ax.hist(x, bins='sqrt')
###

import numpy as np
import matplotlib.pyplot as plt

# Sample data
values = np.random.normal(loc=0, scale=1, size=1000)  # Generate 1000 random values from a normal distribution

# Create histograms with different binning strategies
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

bin_types = ['auto', 'sturges', 'fd', 'sqrt']

for ax, bin_type in zip(axs.flatten(), bin_types):
    counts, bins, patches = ax.hist(values, bins=bin_type, color='lightblue', edgecolor='black', linewidth=1.5, alpha=0.7, density=True)

    print(f"Bin type: {bin_type}")
    print("Counts:", counts)  # Number of data points in each bin
    print("Bins:", bins)      # The edges of the bins
    print("Patches:", patches)  # The bar containers (patches) for each
    for patch in patches:
        print("Patch:", patch)  # Each patch corresponds to a bar in the histogram

    ax.set_title(f'Histogram with bins="{bin_type}"')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.grid(axis='y', alpha=0.75)

fig.tight_layout()
plt.show()
