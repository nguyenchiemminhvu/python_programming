###
# Histogram - PDF
#
# PDF (Probability Density Function) is a function that describes the likelihood of a random variable taking on a particular value. In the context of histograms, when the density parameter is set to True, the histogram is normalized to form a probability density. This means that the area under the histogram will sum to 1, and the height of each bar will represent the probability density of data points in that bin.
#
# To create a histogram with PDF, set the density parameter to True in the ax.hist() function. This will normalize the histogram so that the area under the bars equals 1. Then overlay a PDF curve on top of the histogram to visualize the distribution of the data. You can use scipy.stats.norm.pdf() to calculate the PDF values for a normal distribution.
#
# How to calculate PDF values:
# 1. Import the necessary libraries:
#    from scipy.stats import norm
# 2. Calculate the mean and standard deviation of your data:
#    mean = np.mean(data)
#    std = np.std(data)
# 3. Create an array of x values that span the range of your data:
#    x = np.linspace(min(data), max(data), 100)
# 4. Calculate the PDF values for the x array:
#    pdf = norm.pdf(x, mean, std)
# 5. Plot the histogram and the PDF curve:
#    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
#    ax.plot(x, pdf, 'k', linewidth=2)
###

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Sample data
values = np.random.normal(loc=0, scale=1, size=1000)

# Create a histogram with PDF
fig, ax = plt.subplots(figsize=(10, 6))
counts, bins, patches = ax.hist(values, bins=30, density=True, alpha=0.6, color='g')

# Calculate mean and standard deviation
mean = np.mean(values)
std = np.std(values)

# Create an array of x values
x = np.linspace(min(values), max(values), 100)

# Calculate PDF values
pdf = norm.pdf(x, mean, std)
print(pdf)  # Print the PDF values for debugging

# Plot the PDF curve
ax.plot(x, pdf, 'k', linewidth=2, label='PDF')

# self-calculating pdf for drawing the curve
pdf_self_calculated = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
ax.plot(x, pdf_self_calculated, 'r--', linewidth=2, label='Self-calculated PDF')

ax.legend()
plt.show()