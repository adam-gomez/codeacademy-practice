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

# plt.legend() can also take a keyword argument loc, which will position the legend on the figure.

# These are the position values loc accepts:
# Number Code --- String
# 0 --- best
# 1 --- upper right
# 2 --- upper left
# 3 --- lower left
# 4 --- lower right
# 5 --- right
# 6 --- center left 
# 7 --- center right
# 8 --- lower center
# 9 --- upper center
# 10 --- center

#create your legend here
legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']
plt.legend(legend_labels, loc = 8)
plt.show()

# Modifying Ticks
# Ticks can be modified by either using plt.xticks(), plt.xticklabels(), & plt.xlabel() if you only have one plot
# Or they can be applied to individual subplots by first creating an axes object by using ax = plt.subplot()
# Once the axes object is created, ax.set_xticks(), ax.set_xticklabels(), ax.set_yticks(), ax.set_yticklabels() can be used

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot(1,1,1)
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])
plt.show()

# In order to be sure that you don’t have any stray lines, you can use the command plt.close('all') 
# to clear all existing plots before you plot a new one.

# Sometimes, we would rather have two separate figures. 
# We can use the command plt.figure() to create new figures and size them how we want. 
# We can add the keyword figsize=(width, height) to set the size of the figure, in inches. 
# We can use the command plt.savefig() to save out to many different file formats, such as png, svg, or pdf.

plt.close('all')
plt.figure(figsize=(4,4))
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')

plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')

# Review
x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

y1 = [29.8, 30.1, 30.5, 30.6, 31.3, 31.7, 32.6, 33.1, 32.7, 32.8]

y2 = [32.7, 45.6, 50.9, 49.7, 49.6, 37.3, 26.1, 34.1, 10.9, 21.7]

plt.plot(x, y1, color='pink', marker='o', label='Grumple Consumption')
plt.plot(x, y2, color='gray',marker='o', label='Frumple Consumption')
plt.title('Two Lines on One Graph')
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
ax = plt.subplot(1, 1, 1)
ax.set_xticks(x)
ax.set_xticklabels(['Beans', 'Fruit', 'Allen', 'Saturn', 'Math', 'Elements', 'JohnBolby', 'Eight', 'Nein!', 'End'])
plt.legend(loc=4)
plt.axis([2004, 2008, 15, 45])
plt.show()