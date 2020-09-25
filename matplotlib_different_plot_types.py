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

# ------ BAR CHART WITH ERROR --------
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# create a figure of width 10 and height 8.
plt.figure(figsize=(10,8))
# Plot the blue bars, which have the heights listed in past_years_averages.
# Add error bars of cap size 5 and heights corresponding to the list error.
plt.bar(range(len(past_years_averages)), past_years_averages, yerr = error, capsize=5)
# Set the axis to go from -0.5 to 6.5 on the x-axis and 70 to 95 on the y-axis.
plt.axis([-0.5, 6.5, 70, 95])
# Create an ax object using plt.subplot(). Use ax to set the x-axis ticks to be range(len(years)) and the x-axis labels to be the years list.
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
# Add the title "Final Exam Averages", x-axis label "Year", and y-axis label "Test average".
plt.title('Final Exam Averages')
plt.ylabel('Test average')
plt.xlabel('Year')
# Save your figure to a file called my_bar_chart.png.
plt.savefig('my_bar_chart.png')

plt.show()

# ------ SIDE BY SIDE BARS -------
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

# make the lists school_a_x and school_b_x which will determine where to put the bars for Middle School A and Middle School B along the x-axis.

school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)

#Create a figure of width 10 and height 8.
plt.figure(figsize=(10,8))

# Create a set of axes and save them to ax.
ax = plt.subplot()

# Plot a set of bars representing middle_school_a and a set representing 
# middle_school_b next to each other on the same graph.
plt.bar(school_a_x, middle_school_a, label='Middle School A')
plt.bar(school_b_x, middle_school_b, label='Middle School B')

# Create a new list of x-values called middle_x, which are the values 
# in the middle of school_a_x and school_b_x. This is where we will place the x-ticks. 
# Look at the final graph to see this placement.
middle_x = [(a+b)/2 for a, b in zip(school_a_x, school_b_x)]

# Set the x-ticks to be the middle_x list.
ax.set_xticks(middle_x)

# Set the x-tick labels to be the list unit_topics.
ax.set_xticklabels(unit_topics)

# Create a legend, as shown in the final graph, that labels the first set of bars Middle School A and the second set of bars Middle School B.
plt.legend()

# Create a title (“Test Averages on Different Units”), 
# x-axis label (“Unit”), and y-axis label (“Test Average”).
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')

# Save your figure to a file called my_side_by_side.png.
plt.savefig('my_side_by_side.png')

# ------- STACKED BARS -------
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

# The Bs bars will go on top of the As bars, but at what heights will the Cs, Ds, and Fs bars start?
# The bottom of the bars representing the Cs will be at the height of the As plus the Bs. 
# We can do this in NumPy with the np.add function. c_bottom, the starting heights for the Cs, will be:

c_bottom = np.add(As, Bs)

#create d_bottom and f_bottom here

d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

#create your plot here
# Create a figure of width 10 and height 8.
plt.figure(figsize=(10,8))

# Plot the As, Bs, Cs, Ds, and Fs. 
# Give each one the appropriate bottom list that will stack them on top of each other.
plt.bar(x, As, label='As')
plt.bar(x, Bs, bottom=As, label='Bs')
plt.bar(x, Cs, bottom=c_bottom, label='Cs')
plt.bar(x, Ds, bottom=d_bottom, label='Ds')
plt.bar(x, Fs, bottom=f_bottom, label='Fs')

# Create a set of axes and save them to ax.
ax = plt.subplot(1, 1, 1)
# Set and label the x-ticks
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)

# Give title and axis labels
plt.title('Grade distribution')
plt.ylabel('Number of Students')
plt.xlabel('Unit')

# Add legend
plt.legend()
plt.show()

plt.savefig('my_stacked_bar.png')

# ------- TWO HISTOGRAMS ON A PLOT -------
exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

# Make your plot here
# Create a figure of width 10 and height 8.
plt.figure(figsize=(10, 8))

# Make a histogram of the exam_scores1, normalized, with 12 bins.
plt.hist(exam_scores1, bins = 12, normed=True, histtype='step', linewidth = 2, label = '1st Yr Teaching')

# Make a histogram of the exam_scores2, normalized, with 12 bins.
plt.hist(exam_scores2, bins = 12, normed=True, histtype='step', linewidth = 2, label = '2nd Yr Teaching')

plt.legend()
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.title('Final Exam Score Distribution')
plt.show()
plt.savefig('my_histogram.png')

# ------- LABELED PIE CHART -------

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]
# Create a figure of width 10 and height 8.
plt.figure(figsize=(10,8))

# Plot the num_hardest_reported list as a pie chart
# Label the slices with the unit_topics list and 
# put a percentage label on each slice, rounded to the nearest int.
plt.pie(um_hardest_reported, labels=unit_topics, autopct='%1d%%')

# Set the axes to be 'equal'.
plt.axis('equal')

# Add the title "Hardest Topics".
plt.title('Hardest Topics')

plt.show()

plt.savefig('my_pie_chart.png')

# ------- LINE WITH SHADED ERROR -------
hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]

# Create your figure here
plt.figure(figsize=(10,8))
# Create your hours_lower_bound and hours_upper_bound lists here 
hours_lower_bound = [hours * .80 for hours in hours_reported]

hours_upper_bound = [hours * 1.20 for hours in hours_reported]
# Make your graph here
plt.plot(exam_scores, hours_reported, linewidth = 2)
plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)

plt.title('Time spent studying vs final exam scores')
plt.xlabel('Score')
plt.ylabel('Hours studying (self-reported)')

plt.show()

plt.savefig('my_line_graph.png')