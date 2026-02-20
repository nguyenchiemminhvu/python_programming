###
# In this example, we will visualize multiple line on the same axes using matplotlib.
#
# We can do this by simply calling the 'plot()' function multiple times on the same axes object.
#
# Experience: Never use more than 2 y-axes on the same plot, as it can make the plot difficult to read and interpret. If you need to visualize more than 2 variables, consider using subplots or other types of visualizations.
###

import numpy as np
import matplotlib.pyplot as plt

duration = 10 # 10 seconds
time_arr = np.linspace(0, duration, 1000) # Time array from 0 to 10 seconds with 1000 points
rpm_arr = 1000 + 500 * np.sin(2 * np.pi * time_arr / duration) # RPM array as a sine wave, amplitude of 500, offset of 1000

throttle_arr = 50 + 30 * np.cos(2 * np.pi * time_arr / duration) # Throttle array as a cosine wave, amplitude of 30, offset of 50

figure, ax1 = plt.subplots(figsize=(10, 4)) # Create a figure and an axes

ax1.plot(time_arr, rpm_arr, label="RPM vs time", color='red') # Plot RPM vs time on the axes
ax1.set_title("RPM and Throttle vs Time Plot") # Set the title of the plot
ax1.set_xlabel("Time (seconds)") # Set the x-axis label
ax1.set_ylabel("Engine Speed (RPM)") # Set the y-axis label
ax1.tick_params(axis='y', labelcolor='red') # Set the y-axis tick parameters to match the color of the RPM line
line1, label1 = ax1.get_legend_handles_labels() # Get the handles and labels for the legend from the first axes
ax1.grid(True, which='both', linestyle='--', linewidth=0.5) # Add a grid to the plot

ax2 = ax1.twinx() # Create a second y-axis that shares the same x-axis
ax2.plot(time_arr, throttle_arr, label="Throttle vs time", color='blue')
ax2.set_ylabel("Throttle (%)") # Set the y-axis label for the second y-axis
ax2.tick_params(axis='y', labelcolor='blue') # Set the y-axis tick parameters to match the color of the throttle line
line2, label2 = ax2.get_legend_handles_labels() # Get the handles and labels for the legend from the second axes

ax1.legend(line1 + line2, label1 + label2, loc='upper right') # Add a legend to the first axes, combining the handles and labels from both axes, located at the upper right inside the plot area

plt.title("RPM and Throttle vs Time Plot") # Set the title of the plot
plt.tight_layout() # Adjust the layout to prevent overlap of labels and titles
plt.show() # Display the plot
