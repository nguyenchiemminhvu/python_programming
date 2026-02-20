###
# Grouped Bar Chart
###

import numpy as np
import matplotlib.pyplot as plt

# Sample data
dates = ['2024-01', '2024-02', '2024-03', '2024-04']
usd = [100, 150, 120, 130]
eur = [90, 140, 110, 120]

# Create a grouped bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(dates))

bar1 = ax.bar(index, usd, bar_width, label='USD', color='blue', edgecolor='black', linewidth=1.5)
bar2 = ax.bar(index + bar_width, eur, bar_width, label='EUR', color='green', edgecolor='black', linewidth=1.5)

ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Grouped Bar Chart Example')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(dates)
ax.legend()

plt.show()