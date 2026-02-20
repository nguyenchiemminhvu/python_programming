###
# In this tutorial, we will learn how to create multiple subplots in a single figure using matplotlib.
#
# Matplotlib provides a convenient way to create multiple subplots using the 'plt.subplots()' function.
# The 'plt.subplots()' function returns a figure and an array of axes objects.
# We can specify the number of rows and columns of subplots we want to create by passing the 'nrows' and 'ncols' parameters to the 'plt.subplots()' function.
###

import numpy as np
import matplotlib.pyplot as plt

# prepare data
duration = 10 # seconds
time_arr = np.linspace(0, duration, num=100) # 100 data points from 0 to duration
rpm_data = 1000 + 500 * np.sin(2 * np.pi * time_arr / duration) # simulate RPM data as a sine wave
throttle_data = 50 + 30 * np.cos(2 * np.pi * time_arr / duration) # simulate throttle position data as a cosine wave
speed_data = 80 + 20 * np.sin(2 * np.pi * time_arr / duration + np.pi / 4) # simulate speed data as a sine wave with a phase shift

# Create a figure and an array of axes objects with 2 rows and 1 column
figure, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 8), sharex=True) # sharex=True means that the x-axis will be shared among all subplots

axes[0].plot(time_arr, rpm_data, label='RPM', color='green')
axes[0].set_title('RPM Over Time')
# axes[0].set_xlabel('Time (s)') # when using sharex=True, we only need to set the x-axis label for the last subplot
axes[0].set_ylabel('RPM')
axes[0].legend()

axes[1].plot(time_arr, throttle_data, label='Throttle Position', color='blue')
axes[1].set_title('Throttle Position Over Time')
# axes[1].set_xlabel('Time (s)') # when using sharex=True, we only need to set the x-axis label for the last subplot
axes[1].set_ylabel('Throttle Position (%)')
axes[1].legend()

axes[2].plot(time_arr, speed_data, label='Speed', color='red')
axes[2].set_title('Speed Over Time')
axes[2].set_xlabel('Time (s)') # when using sharex=True, we only need to set the x-axis label for the last subplot
axes[2].set_ylabel('Speed (km/h)')
axes[2].legend()

# Exp: recommend always enable grid for better readability of the plots
for ax in axes:
    ax.grid(True, linestyle='--', alpha=0.5)

figure.align_ylabels() # align y-axis labels for better aesthetics

plt.suptitle("Vehicle Data Over Time", fontsize=16) # set a common title for the entire figure
plt.tight_layout()
plt.show()