import pandas as pd

orders = pd.read_csv('orders.csv')
# Examine the first 10 rows
print(orders.head(10))
# price of the most expensive pair of shoes purchased
most_expensive = orders.price.max()
# how many different colors of shoes we are selling
num_colors = orders.shoe_color.nunique()
# the most expensive shoe for each shoe_type
pricey_shoes = orders.groupby('shoe_type').price.max()
# Modify your code from the previous exercise so that it ends with reset_index, which will change pricey_shoes into a DataFrame.
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
# Calculate the 25th percentile for shoe price for each shoe_color
cheap_shoes = orders.groupby('shoe_color').price\
    .apply(lambda x: np.percentile(x, 25))\
        .reset_index()
# Create a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased. Save it to the variable shoe_counts.
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
# compare purchases of different shoe colors of the same shoe type by creating a pivot table.
shoe_counts_pivot = shoe_counts.pivot(columns = 'shoe_color', index = 'shoe_type', values = 'id').reset_index()
print(shoe_counts_pivot)

# Use a groupby statement to calculate how many visits came from each of the different sources. Save your answer to the variable click_source.
click_source = user_visits.groupby('utm_source').id.count().reset_index()
click_source.rename(columns = {'id':'count'}, inplace = True)
print(click_source)

# Use groupby to calculate the number of visits to our site from each utm_source for each month. Save your answer to the variable click_source_by_month.
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

# Use pivot to create a pivot table where the rows are utm_source and the columns are month. Save your results to the variable click_source_by_month_pivot
click_source_by_month_pivot = click_source_by_month.pivot(columns = 'month', index = 'utm_source', values = 'id').reset_index()
print(click_source_by_month_pivot)

# Examine the first few rows of ad_clicks.
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

# ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week.

import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# print(ad_clicks.head())

#How many views (i.e., rows of the table) came from each utm_source?
utm_source_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(utm_source_views)

#Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks.head())

# percent of people who clicked on ads from each utm_source.
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
#print(clicks_by_source)
# clicks_by_source pivoted for clarity
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()
#print(clicks_pivot)

# percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[False] + clicks_pivot[True])

# Analyzing an A/B Test
# The column experimental_group tells us whether the user was shown Ad A or Ad B.

# Were approximately the same number of people shown both adds? Yes

experimental_group_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
experimental_group_count.rename(columns={'user_id':'count'}, inplace=True)
#print(experimental_group_count)

# Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.

#print(clicks_pivot)
# Creating a pivot table showing experimental group by is_click 
percentage_click = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
percentage_click_pivot = percentage_click.pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index()
#adding percentage to pivot table
percentage_click_pivot['percentage'] = percentage_click_pivot[True] / (percentage_click_pivot[True] + percentage_click_pivot[False])

#print(percentage_click_pivot)
#Ad A had 37.5% engagement, Ad B had 30.8% engagement

# The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

# Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
print(a_clicks.head())
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(b_clicks.head())
#For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.
a_clicks_percent = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()

b_clicks_percent = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()

a_clicks_percent_pivot = a_clicks_percent.pivot(columns='is_click', index = 'day', values='user_id')

b_clicks_percent_pivot = b_clicks_percent.pivot(columns='is_click', index ='day', values='user_id')

a_clicks_percent_pivot['percentage'] = a_clicks_percent_pivot[True] / (a_clicks_percent_pivot[True] + a_clicks_percent_pivot[False])

b_clicks_percent_pivot['percentage'] = b_clicks_percent_pivot[True] / (b_clicks_percent_pivot[True] + b_clicks_percent_pivot[False])

print(a_clicks_percent_pivot)
print(b_clicks_percent_pivot)
# Ad A is outperforming Ad B on every day except Tuesday
# Recommendation to continue Ad A, discontinue Ad B

df1 = pd.DataFrame({
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday']})

print(a_clicks_percent_pivot['percentage'])

df1['percent_diff_a_minus_b'] = a_clicks_percent_pivot.percentage * 100 - b_clicks_percent_pivot.percentage * 100
print(df1)