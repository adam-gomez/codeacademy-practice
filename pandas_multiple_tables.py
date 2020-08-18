import pandas as pd
# The .merge method looks for columns that are common between two DataFrames and then looks for rows where those column’s values are the same. It then combines the matching rows into a single row in a new table.
# new_df = pd.merge(orders, customers)
# There are two DataFrames defined in the file
sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)
# Create a new DataFrame sales_vs_targets which contains the merge of sales and targets.
sales_vs_targets = pd.merge(sales, targets, left_on = 'month', right_on = 'month', how = 'inner')

print(sales_vs_targets)
# Select the rows from sales_vs_targets where revenue is greater than target. Save these rows to the variable crushing_it.
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

# In addition to using pd.merge, each DataFrame has its own merge method. 
# For instance, if you wanted to merge orders with customers, you could use:

# new_df = orders.merge(customers)
#This produces the same DataFrame as if we had called pd.merge(orders, customers).

# We generally use this when we are joining more than two DataFrames together because 
# we can “chain” the commands. 
# The following command would merge orders to customers, 
# and then the resulting DataFrame to products:

# big_df = orders.merge(customers)\
#     .merge(products)

# We have some more data from Cool T-Shirts Inc. 
# The number of men’s and women’s t-shirts sold per month is in a file called men_women_sales.csv. 
# Load this data into a DataFrame called men_women.
men_women = pd.read_csv('men_women_sales.csv')

# Merge all three DataFrames (sales, targets, and men_women) into one big DataFrame called all_data.
all_data = sales.merge(targets).merge(men_women)

# Display all_data using print.
print(all_data)

# Select the rows of all_data where:

# revenue is greater than target
# AND

# women is greater than men
# Save your answer to the variable results.

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

# Merge orders and products using rename. Save your results to the variable orders_products.
orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))

# Pandas won’t let you have two columns with the same name, so it will change them to column_x and column_y.
# The new column names column_x and column_y aren’t very helpful for us when we read the table. 
# We can help make them more useful by using the keyword suffixes.
# Merge orders and products using left_on and right_on. Use the suffixes _orders and _products.
# Save your results to the variable orders_products.
orders_products = pd.merge(orders, products, left_on='product_id', right_on='id', how='inner', suffixes=['_orders','_products'])

# can we merge on more than one specific column?
# Yes, you can perform a merge on one column, or on multiple specified columns, by passing in a list of the column names for each dataframe.
# When listing multiple column names, it will only return rows for which all the column values match. 
# Furthermore, the number of columns listed must match, and the order they are listed will matter.

#can we set another value to take place of missing values instead of None or nan?
# After the merge, replacing these is a bit easier. You can utilize the fillna() method, which will replace all missing or nan values with another value you specify.
# Replaces all nan values with 0
df.fillna(0, inplace=True)

tore_a_b_left = pd.merge(store_a, store_b, how='left')
print(store_a_b_left)

store_b_a_left = pd.merge(store_b, store_a, how='left')
print(store_b_a_left)

#An ice cream parlor and a bakery have decided to merge.

#The bakery’s menu is stored in the DataFrame bakery, and the ice cream parlor’s menu is stored in DataFrame ice_cream.

#Create their new menu by concatenating the two DataFrames into a DataFrame called menu.

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery, ice_cream])
print(menu)

#Cool T-Shirts Inc. just created a website for ordering their products. They want you to analyze two datasets for them:

#visits contains information on all visits to their landing page
#checkouts contains all users who began to checkout on their website
#Use print to inspect each DataFrame.
visits = pd.read_csv('visits.csv', parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv', parse_dates=[1])

print(visits)
print(checkouts)

#We want to know the amount of time from a user’s initial visit to the website to when they start to check out.
v_to_c = pd.merge(visits, checkouts)

v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time

print(v_to_c)
print(v_to_c.time.mean())

# Page Visits Funnel
visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart_lmerge = pd.merge(visits, cart, how = 'left')

# How long is your merged DataFrame?
print(visits_cart_lmerge.shape)

print(visits_cart_lmerge['cart_time'].isnull().sum())
# 1652 cart_time values are NaN. These are customers who visited the website, but never added a t-shirt to their cart

# Note: It is no longer necessary in current version of python to turn integers into float values before dividing
# This tutorial is running in an earlier python environment
percentage_not_cart = visits_cart_lmerge['cart_time'].isnull().sum().astype('float') / len(visits_cart_lmerge.index) * 100
print(percentage_not_cart)

cart_checkout_lmerge = pd.merge(cart, checkout, how = 'left')
percentage_not_checkout = cart_checkout_lmerge['checkout_time'].isnull().sum().astype('float') / len(cart_checkout_lmerge.index) * 100
print(percentage_not_checkout)
# 25.31% of people with a t-shirt in their cart did not checkout

all_data = pd.merge(visits, cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')
print(all_data.head())

checkout_purchase_lmerge = pd.merge(checkout, purchase, how = 'left') 

percentage_not_purchase = checkout_purchase_lmerge['purchase_time'].isnull().sum().astype('float') / len(checkout_purchase_lmerge.index) * 100
#print(percentage_not_purchase)

print(percentage_not_cart)
print(percentage_not_checkout)
print(percentage_not_purchase)
#83% of user put an item in their cart, of those, 25% will move to checkout, of those 17% will complete a purchase. 

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)

print(all_data.time_to_purchase.agg('mean'))
