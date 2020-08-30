#Lesson Goals:
# Creating a line graph from data
# Changing the appearance of the line
# Zooming in on different parts of the axis
# Putting labels on titles and axes
# Creating a more complex figure layout
# Adding legends to graphs
# Changing tick labels and positions
# Saving what you’ve made

from matplotlib import pyplot as plt

# Basic Line Plot
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
plt.plot(x_values, y_values)
plt.show()

days = list(range(7))
money_spent = [10,12,12,10,14,22,24]

# Plot days on the x-axis and money_spent on the y-axis using plt.plot().
plt.plot(days, money_spent)
plt.show()

# We can also have multiple line plots displayed on the same set of axes.
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
# Plot your money:
plt.plot(days, money_spent)
# Plot your friend's money:
plt.plot(days, money_spent_2)
# Display the result:
plt.show()

# We have defined lists called time, revenue, and costs. Plot revenue vs time.
# Plot costs vs time on the same plot.

revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()

# Linestyles
# We can specify a different color for a line by using the keyword color with either an HTML color name or a HEX code:
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')

# We can also make a line dotted or dashed using the keyword linestyle.
# Dashed:
plt.plot(x_values, y_values, linestyle='--')
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
# No line:
plt.plot(x_values, y_values, linestyle='')

# We can also add a marker using the keyword marker:
# A circle:
plt.plot(x_values, y_values, marker='o')
# A square:
plt.plot(x_values, y_values, marker='s')
# A star:
plt.plot(x_values, y_values, marker='*')

# Plot revenue vs. time as a purple ('purple'), dashed ('--') line.
plt.plot(revenue, time, color = 'purple', linestyle = '--')
#Plot costs vs. time as a line with the HEX color #82edc9 and square ('s') markers.
plt.plot(costs, time, color = '#82edc9', marker = 's')

plt.show()

# Axis and Labels
# Sometimes, it can be helpful to zoom in or out of the plot, especially if there is some detail we want to address. To zoom, we can use plt.axis(). We use plt.axis() by feeding it a list as input. This list should contain:

# The minimum x-value displayed
# The maximum x-value displayed
# The minimum y-value displayed
# The maximum y-value displayed
# plt.axis([x_min, x_max, y_min, y_max])
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0,12,2900,3100])

plt.show()

# Labeling the Axes
# We can label the x- and y- axes by using plt.xlabel() and plt.ylabel(). The plot title can be set by using plt.title().
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])

plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')

plt.show()

# Subplots
# We can create subplots using .subplot().

# The command plt.subplot() needs three arguments to be passed into it:

# The number of rows of subplots
# The number of columns of subplots
# The index of the subplot we want to create
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

# Using the plt.subplot command, plot temperature vs months in the left box of a figure that has 1 row with 2 columns.
plt.subplot(1, 2, 1)
plt.plot(temperature, months)


# Plot flights_to_hawaii vs temperature in the same figure, to the right of your first plot. Add the parameter "o" to the end of your call to plt.plot to make the plot into a scatterplot, if you want!
plt.subplot(1, 2, 2)
plt.plot(flights_to_hawaii, temperature, 'o')

plt.show()

# We can customize the spacing between our subplots to make sure that the figure we create is visible and easy to understand. To do this, we use the plt.subplots_adjust() command.
# left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
# right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend
# bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
# top — the top margin, with a default of 0.9
# wspace — the horizontal space between adjacent subplots, with a default of 0.2
# hspace — the vertical space between adjacent subplots, with a default of 0.2

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace = 0.35, bottom = 0.2)
plt.show()

# Legends
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here
legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']
plt.legend(legend_labels, loc = 8)
plt.show()