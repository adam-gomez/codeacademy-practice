# Lesson Goals
# Compare categories of data with bar graphs
# Show uncertainty in data using error bars and shading
# Compare proportional datasets using pie charts
# Analyze frequency data using histograms

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)
plt.show()
# This creates a bar plot that has ambiguous x-axis values

plt.bar(range(len(drinks)), sales)

#By adding in an axes object and setting the xticks and their labels, we can create a less ambiguous chart
ax = plt.subplot(1,1,1)
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()

# Creating side by side bar charts
# If we want to compare the heights of adjacent bars, we can use a bit of code to ensure that the position
# of each bar on the x-axis is incremented so that the bars do not overlap and the bars are touching
# The spacing between each comparison is based on the number of bars represented (2, 3, etc.)
# So our formula must account for the possibility of different number of bars being clustered together
# The following code will suffice for this task:
# n = ?  # This is our second dataset (out of 2)
# t = ? # Number of datasets
# d = ? # Number of sets of bars
# w = ? # Width of each bar
# x_values = [t*element + w*n for element in range(d)]

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]

n = 2 # This is the second dataset (out of 2)
store2_x = [t*element + w*n for element in range(d)]

plt.bar(store1_x, sales1)
plt.bar(store2_x, sales2)
plt.show()

# Creating a stacked bar chart can be made by setting the bottom edge of the bars to be graphed
# By setting the bottoms of the second set of graphs to be equal to the tops of the first set of graphs
# The bars will be perfectly stacked on top of each other

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

ax = plt.subplot(1,1,1)
plt.bar(range(len(drinks)), sales1, label='Location 1')
plt.bar(range(len(drinks)), sales2, bottom=sales1, label='Location 2')
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.legend()

plt.show()

# Error bars can be used to show uncertainty in the data
# The horizontal lines at the top and bottom are called caps
# We can set the size of the error bar by adding yeer=# to our plt.bar command
# If we want a different amount of error on each bar, we can set the yeer equal to a list (yeer=listyeer)
# We can also set the width of the cap ends with capsize=#

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

ax = plt.subplot(1,1,1)
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()

