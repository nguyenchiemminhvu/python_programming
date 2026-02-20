###
# Practice with histograms
#
# Histogram is a type of plot that shows the distribution of a dataset. It is created by dividing the data into bins and counting the number of data points that fall into each bin. The height of each bar in the histogram represents the frequency of data points in that bin.
#
# Histograms answer questions like:
# - How is the data distributed?
# - Are there any outliers?
# - What is the central tendency of the data?
#
# ax.hist(x,
#         bins=None,
#         range=None,
#         density=False,
#         cumulative=False,
#         histtype='bar',
#         alpha=None)
#
# Key parameters:
# - x: The input data (array-like).
# - bins: The number of bins or the edges of the bins.
# - range: The lower and upper range of the bins.
# - density: If True, the histogram is normalized to form a probability density.
# - cumulative: If True, the histogram is cumulative.
# - histtype: The type of histogram to draw ('bar', 'barstacked', 'step', 'stepfilled').
# - alpha: The transparency of the bars (0.0 to 1.0).
###

import numpy as np
import matplotlib.pyplot as plt

# Sample data
freq = [1, 10, 15, 7, 12, 20, 5, 8, 18, 25, 30, 22, 17, 14, 9, 11]

# Create a histogram
fig, axs = plt.subplots(figsize=(10, 6), nrows=2, ncols=1)

counts, bins, patches = axs[0].hist(freq, bins=5, color='lightblue', edgecolor='black', linewidth=1.5, alpha=0.7, density=False)
# The freq array will be distributed into 5 bins, and the height of each bar will represent the count of data points in that bin.
# Bins: [1-6], [7-12], [13-18], [19-24], [25-30]

# Debug counts, bins, and patches
print("Counts:", counts)  # Number of data points in each bin
print("Bins:", bins)      # The edges of the bins
print("Patches:", patches)  # The bar containers (patches) for each bin
for patch in patches:
    print("Patch:", patch)  # Each patch corresponds to a bar in the histogram

axs[0].set_xlabel('Frequency')
axs[0].set_ylabel('Count')
axs[0].set_title('Histogram Example')

axs[0].grid(axis='y', alpha=0.75)  # Add grid lines for better readability

axs[1].hist(freq, bins=5, color='lightcoral', edgecolor='black', linewidth=1.5, alpha=0.7, cumulative=True, density=True, histtype='stepfilled')

plt.show()
