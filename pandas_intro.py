import pandas as pd

df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)

df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=['Store ID', 'Location', 'Number of Employees'
    #add column names here
  ])

print(df2)

'''
The first row of a CSV contains column headings. 
All subsequent rows contain values. 
Each column heading and each variable is separated by a comma.
'''

df = pd.read_csv('sample.csv')
print(df)

df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north
print(type(clinic_north))
print(type(df))

clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))

march = df.iloc[2]
april_may_june = df.iloc[3:]
print(april_may_june)

january = df[df['month'] == 'January']
print(january)

march_april = df[(df.month == 'March') | (df.month == 'April')]

print(march_april)

january_february_march = df[df.month.isin(['January', 'February', 'March'])]

print(january_february_march)

df2 = df.loc[[1, 3, 5]]

# print(df2)

df3 = df2.reset_index()

print(df3)

df2.reset_index(inplace = True, drop = True)

print(df2)

#Part 1: reading the csv
orders = pd.read_csv('shoefly.csv')

#Part 2: inspecting the first five lines of data
print(orders.head(5))

#Part 3: selecting the column 'email'
emails = orders.email

#Part 4: the Frances Palmer incident
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

#Part 5: Comfy feet means more time on the street
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]

# One way that we can add a new column is by giving a list of the same length as the existing DataFrame.
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

# We can also add a new column that is the same for all rows in the DataFrame. 
df['In Stock?'] = True
df['Is taxed?'] = 'Yes'
print(df)

# you can add a new column by performing a function on the existing columns.
df['Margin'] = df.Price - df['Cost to Manufacture']
print(df)

#We can use the apply function to apply a function to every value in a particular column.
from string import lower
df['Lowercase Name'] = df.Name.apply(lower)
print(df)

#Reviewing Lambda Function
stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!"))
mylambda = lambda x: x[0]+x[-1]
print(mylambda('Hello World'))

# lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]
mylambda = lambda age: "Welcome to BattleCity!" if age >= 13 else 'You must be over 13'


# Create a lambda function get_last_name which takes a string with someone’s first and last name (i.e., John Smith), and returns just the last name (i.e., Smith).
get_last_name = lambda name: name.split(' ')[-1]
# Use the lambda function get_last_name to create a new column last_name with only the employees’ last name.
df['last_name'] = df.name.apply(get_last_name)

# WE CAN ALSO OPERATE ON MULTIPLE COLUMNS AT ONCE. If we use apply without specifying a single column and add the argument axis=1, the input to our lambda function will be an entire row, not a column.
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)

# Renaming Columns
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

# Tou also can rename individual columns by using the .rename method. Pass a dictionary
df.rename(columns={'name': 'movie_title'}, inplace=True)

orders = pd.read_csv('shoefly.csv')

#Examine the first 5 rows of the data using print and head.
print(orders.head())

# Add a new column called shoe_source, which is vegan if the materials is not leather and animal otherwise.
orders['shoe_source'] = orders.shoe_material.apply(lambda x: 'animal' if x == 'leather' else 'vegan')

#Using the columns last_name and gender create a column called salutation which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.
orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row.last_name if row.gender == 'male' else 'Dear Ms. ' + row.last_name, axis = 1)

#Data for all of the locations of Petal Power is in the file inventory.csv. Load the data into a DataFrame called inventory.
import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')

# Inspect the first 10 rows of inventory.
print(inventory.head(10))

# The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.
staten_island = inventory.iloc[0:10]

# A customer just emailed you asking what products are sold at your Staten Island location. Select the column product_description from staten_island and save it to the variable product_request.
product_request = staten_island.product_description

# Another customer emails to ask what types of seeds are sold at the Brooklyn location. Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request.
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

# Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)

# Petal Power wants to know how valuable their current inventory is. Create a column called total_value that is equal to price multiplied by quantity.
inventory['total_value'] = inventory.price * inventory.quantity

# The Marketing department wants a complete description of each product for their catalog. The following lambda function combines product_type and product_description into a single string:
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

# Using combine_lambda, create a new column in inventory called full_description that has the complete description of each product.
inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)