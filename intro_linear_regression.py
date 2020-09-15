# -- Introduction to Linear Regression -- 

# Creating a model that explains data to predict what may happen next
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

plt.plot(months, revenue, "o")

plt.title("Sandra's Lemonade Stand")

plt.xlabel("Months")
plt.ylabel("Revenue ($)")

plt.show()

# Based on eyeballing the produced scatterplot, what do you think the revenue in month 13 would be?
month_13 = 185

# -- Points and Lines --

# A line is determined by its slope and intercept (y = mx + b)
# m = slope; b = intercept; y=prediction based on x=data
# Using just my eyes, it looks like good m and b values are :

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 11
#intercept:
b = 45

y = [month * m + b for month in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()

# -- Loss --

# For each data point, we can calculate *loss*, a number that measures how far the point was from the model's prediction
# This is sometimes referred to as error
# Loss is the squared distance from the line (so that points above and below the line both contribute to total loss in the same way)

# We have three points, (1, 5), (2, 1), and (3, 3). We are trying to find a line that produces lowest loss.
x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0
y_predicted1 = [1, 2, 3] # using the model y = x (m = 1, b = 0), we can predict some y values based off our x's

#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [1.5, 2, 2.5] # like above, but using y = 0.5x + 1 (m = 0.5, b = 1)

# Calculating loss
# We can sum the squared differences between the values in y_predicted1 and y
total_loss1 = 0
for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i]) ** 2

