# -- INTRODUCTION TO LINEAR REGRESSION -- 

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

# ------------------------------------------------------------------------------------

# -- POINTS AND LINES --

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

# ------------------------------------------------------------------------------------

# -- LOSS --

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
# We can sum the squared differences between the values in y_predicted and y
total_loss1 = 0
for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i]) ** 2 # = 17

total_loss2 = 0
for i in range(len(y)):
  total_loss2 += (y[i] - y_predicted2[i]) ** 2 # = 13.5

print(total_loss1, total_loss2)

better_fit = 2 # model 2 has less loss/error than model 1

# ------------------------------------------------------------------------------------

# -- MINIMIZING LOSS --

# Finding the optimal model (least error) is done by a process called gradient descent
# By calculating the loss for every intercept, we create a parabolic graph along N dimensions (where N is the number of parameters/inputs)
# Using calculus, we can find the area of least loss where the slope of the graph reaches 0

# ------------------------------------------------------------------------------------

# -- GRADIENT DESCENT FOR INTERCEPT (B) -- 

# The following function determines the slope at any particular intercept value (b)
def get_gradient_at_b(x, y, m, b):
  diff = 0 # This will store the sum of the differences between a data point (y) and (mx + b) (where m = current gradient guess and b = current intercept guess)
    N = len(x) # Number of points in the dataset
  for i in range(N):
    diff += (y[i] - (m * x[i] + b)) # Calculated for each coordinate and based on the partial derivative of the error function with respect to b
  b_gradient = -2/N * diff 
  return b_gradient
# With the gradient calculated, that data can be used to identify the "direction" that the model needs to adjust the intercept by to find local and global minima (lowest loss numbers)

# ------------------------------------------------------------------------------------

# -- GRADIENT DESCENT FOR SLOPE (M) -- 

# This function is similar to the formula for the intercept, with a slight adjustment in calculating diff
def get_gradient_at_m(x, y, m , b):
  diff = 0
  N = len(x)
  for i in range(N):
    diff += x[i] * (y[i] - ((m * x[i]) + b)) # Based on the partial derivative of the error function with respect to m
  m_gradient = -2/N * diff
  return m_gradient

# ------------------------------------------------------------------------------------

# -- DETERMINING THE STEP GRADIENT -- 

# We can scale the size of the step by multiplying the gradient by a learning rate

# To find a new b value:
new_b = current_b - (learning_rate * b_gradient)
# Where current_b is our guess for what the b value is, b_gradient is the gradient of the loss curve at our current guess
# and learning_rate is proportional to the size of the step we want to take (which we can base off the magnitude of the b_gradient at our current_b)

# This function will find the gradients at b_current and m_current, and return new b and m values that have been "stepped" in the direction toward the local minima of the loss curve 
# The size of the step should be based on the magnitude of the gradient but for now we will hard code it in at a rate of .01
def step_gradient_rate_1_percent (x, y, b_current, m_current):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (0.01 * b_gradient) # Hard coded hyperparameter of .01, the b is stepped in the direction of the downward slope
  m = m_current - (0.01 * m_gradient) # Hard coded hyperparameter of .01, the m is stepped in the direction of the downward slope
  return b, m # The b and m returned from this function will be closer to the local minima of the loss function
  # Calling this function many, many times will continue to move our b and m value closer and closer to the local minima

# Example Data plugged into step_gradient_rate_1_percent() function:
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m
b, m = step_gradient(months, revenue, b, m)
print(b, m) # 2.355 17.78333333333333

# ------------------------------------------------------------------------------------

# -- CONVERGENCE --
# Convergence is when the loss stops changing after parameters have changed
# Hopefully the algorithm will converge at the best values for m and b

# Methods for determining convergence
# GRAPHING:
# By graphing the b value or m value over N iterations, the b value will reach a point where additional iterations do not change b. 
# This b value is the optimal value that minimizes the loss function

# CHOOSING:
# By choosing an arbitrary value such that any loss value below that number is declared to have reached convergence (and subsequent iterations are not necessary)

# ------------------------------------------------------------------------------------

# -- LEARNING RATE --
# The learning rate is the relative size of the step, such that you don't overshoot your minima (and never converge) 
# nor do you step so small that the number of iterations needed to reach the local minima reaches a computationally inefficient number

# ------------------------------------------------------------------------------------

# -- GRADIENT DESCENT FUNCTION --

# We can update our step_gradient function to no longer have a learning rate of 0.01 hard coded, but instead accept a learning rate as a parameter
def step_gradient (x, y, b_current, m_current, learning_rate):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (learning_rate * b_gradient) 
  m = m_current - (learning_rate * m_gradient) 
  return b, m

# We can now create a gradient_descent function that will take in a set of x values, a set of y values
# and apply our step gradient function a number of times (the parameter will be num_iterations)
# with each step gradient calibrated to a learning rate provided (the parameter will be learning_rate)
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0 # initial guess for b
  m = 0 # initial guess for m
  for i in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return b, m

# Testing the function with data
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)

# We can now create our line of best fit using the m and b results from our function
# We create a list of y values using our mx + b where each x in our x values creates a y value
y = [m*x + b for x in months]

plt.plot(months, revenue, "o") # Scatterplot of the raw data
plt.plot(months, y) # We then plot those x values and y values for our line

plt.show()

# ------------------------------------------------------------------------------------

# -- USING SCIKIT-LEARN --

# We don't need to use a scratch-built linear regression algorithm
from sklearn.linear_model import LinearRegression 

# You can first create a LinearRegression model, and then fir it to your x and y data
line_fitter = LinearRegression()
line_fitter.fit(X, y)
    # The .fit() method gives the model two variables that are useful to us
    # the line_fitter.coef_, which contains the slope
    # the line_fitter.intercept_, which contains the intercept

# We can also use the .predict() function to pass in x-values and receive the y-values that this line would predict:
y_predicted = line_fitter.predict(X) 

# Note: The num_iterations and the learning_rate that we coded in our scratch-built linear regression function have default values within sklearn
#       They do not need to be set specifically

# Example of using LinearRegression()

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2)) # creates a 1-D array of temps
temperature = temperature.reshape(-1, 1) # turns the 1-D array into the 2-D array needed for .fit() without changing the data
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

line_fitter = LinearRegression() # Creating an sklearn linear regression model
line_fitter.fit(temperature, sales) # Passing in the temperature and sales data (x, y) into the .fit() function

# We could set the .coef_ and the .intercept_ to variables and print them to visualize them directly

sales_predict = line_fitter.predict(temperature) # generating an array of y-values predicted by passed in x values (temperature) based on the m and b values from .fit()

plt.plot(temperature, sales, 'o') # plot of the raw data (scatterplot)
plt.plot(temperature, sales_predict) # plot of the predicted data (line of best fit)

plt.show()