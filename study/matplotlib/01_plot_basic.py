###
#  Matplotlib is a powerful plotting library in Python that allows you to create a wide variety of static, animated, and interactive visualizations. The basic structure of a Matplotlib plot consists of three main components:
# figure -> axes -> plot elements
# 
# EXP: If truly understand matplotlib, every other visuallization library in python will be easy to learn.
#
# In this example below, we will create a simple line plot of speed vs time using matplotlib. We will generate a time array and a corresponding speed array, then plot them using the plot() function. We will also customize the plot by adding titles, labels, legends, and a grid for better visualization.
#
# Relationship between figure, axes, and plot elements:
# - Figure: The overall container for the plot. It can contain multiple axes.
# - Axes: The area where the data is plotted. It can contain multiple plot elements such as lines, markers, etc.
# - Plot elements: The actual data representations (e.g., lines, points) that are drawn on the axes.
#
# It is recommend to always use fig, axes = plt.subplots() to create a figure and axes, as it provides more control and flexibility over the plotting area.
# Never rely on plt.plot(...) alone, as it can lead to confusion and less control over the plot, especially when dealing with multiple plots or subplots.
# Also recommend to label every plot elements: title, x-axis, y-axis, legend, grid, units... for precise reading value in analysis.
#
#
# matplotlib has two APIs:
# 1. Object-oriented API: This is the recommended way to create plots, because that's how serious analysis is done.
# 2. Pyplot API: This is a simpler interface that is often used for quick plotting, but it can lead to less control and confusion when creating complex plots.
###

import numpy as np
import matplotlib.pyplot as plt

time_arr = np.linspace(0, 10, 1000) # Time array from 0 to 10 seconds with 1000 points
speed_arr = 10 * np.sin(time_arr) # Speed array as a sine wave, amplitude of 10

figure, axes = plt.subplots(figsize=(10, 4)) # Create a figure and an axes

axes.plot(time_arr, speed_arr, label="Speed vs Time", color='blue') # Plot speed vs time on the axes
axes.set_title("Speed vs Time Plot") # Set the title of the plot
axes.set_xlabel("Time (seconds)") # Set the x-axis label
axes.set_ylabel("Speed (units)") # Set the y-axis label
axes.legend() # Add a legend to the plot
axes.grid() # Add a grid to the plot

plt.show() # Display the plot
