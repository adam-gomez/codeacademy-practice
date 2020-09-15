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

# We can similarly represent error on a line graph using fill between
onths = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

y_lower = [num - 0.1 * num for num in revenue]
y_upper = [num * 1.1 for num in revenue]

#your work here
ax = plt.subplot(111)
ax.set_xticks(months)
ax.set_xticklabels(month_names)
plt.fill_between(months, y_lower, y_upper, alpha=0.2)
plt.plot(months, revenue)

plt.show()

# Although pie charts should generally be avoided, we can create a pie chart in matplotlib
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#pie chart here
plt.pie(payment_method_freqs)
plt.axis('equal') #this prevents the pie chart from being shown at an isometric angle
plt.show()

# We can add a legend to our chart by using a label parameter and plt.legend()
# We can add annotations to our chart by using autopct='$0.#f%%'
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.axis('equal')
plt.legend()
plt.show()

# '%d%%' = rounded to the nearest int with % at end
# '0.2f' = 2 decimal places
# We can create histograms easily from data
from script import sales_times #source of data

#create the histogram here
plt.hist(sales_times, bins=20)
plt.show()

# We can normalize our histograms to show relative proportions with data that have different magnitudes
# We can also create an outline of a histogram by using histtype='step'
from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=.4, normed=True)
#plot your other histogram here
plt.hist(sales_times2, bins=20, normed=True, histtype='step')

plt.show()