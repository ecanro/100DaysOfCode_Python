import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('salaries_by_college_major.csv')
# see head cells
print(df.head())
# see rows and columns
print(df.shape)
# only columns
print(df.columns)
# search by NaN cells(blank cells)
print(df.isna())
# check last couple of rows in dataframe
print(df.tail())
# delete the rows with NaN cells
clean_df = df.dropna()
print(clean_df.tail())
# read particular column
clean_df['Starting Median Salary']
# find the hightest salary
clean_df['Starting Median Salary'].max()
# find the hightest salary row->43
clean_df['Starting Median Salary'].idxmax()
# using location for search in rows
clean_df['Undergraduate Major'].loc[43]
# or
clean_df['Undergraduate Major'][43]
#without row name
clean_df.loc[43]

# Day 72
# The Highest Mid-Career Salary
print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]

# The Lowest Starting and Mid-Career Salary
print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]
clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

# Lowest Risk Majors
clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# or
clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

# add this to our existing dataframe
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

# Sorting by the Lowest Spread
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

# Majors with the Highest Potential
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

# Majors with the Greatest Spread in Salaries
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

# use the .groupby() method
clean_df.groupby('Group').count()

# groupby with mean and formating output
pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()

# Day_73
# read our data and format the head cells
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
# see firts 5 rows
print(df.head())
# see last 5 rows
print(df.tail())
# using .shape to see the df dimension
print(df.shape)
# using count to see number of entrys in all columns
print(df.count())
# or using count to see number of entrys in especific columns
print(df.count()['TAG'])
# using group to group data
# with sum to see how many post had every language
print(df.groupby('TAG').sum())
#with count to see how many month exist
print(df.groupby('TAG').count())

## selecting
# an individual cell using braket notation
print(df['DATE'][1])
# or using dot notation
print(df.DATE[1])
# inspect data type
print(type(df.DATE[1]))
# but the DATE format is not very handy (00:00:00?!)
# we can use to_datetime() to convert the type str to date
print(pd.to_datetime(df.DATE[1]))
# convert the DATE column
df.DATE = pd.to_datetime(df.DATE)
print(df.head())

##Data manipulation
#Pivoting DF
#using the .pivot() method
# to set categoryes in columns
#examp:
test_df = pd.DataFrame({
    'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
    'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
    'Power': [100, 80, 25, 50, 99, 75, 5, 30]
     })
print(test_df)
# using pivot
pivote_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivote_df)
# note that if a value is missing, the pivot method insert a NaN value
# in test_df Silvester had a missing value

# pivoting our df
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)
print(reshaped_df.columns)
print(reshaped_df.shape)
print(reshaped_df.count())

# Dealing with NaN Values
# using .fillna() method with inplace to update the DF
reshaped_df =reshaped_df.fillna(0)
print(reshaped_df.head())

# now verify NaN in all DF
reshaped_df.isna().values.any()

#Day_74
#Using Matplotlib
# resizing chart
plt.figure(figsize=(16,10))
#resizing fonts
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# add labels axis
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# add limit to y axis
plt.ylim(0, 35000)
# plot the chart java
plt.plot(reshaped_df.index, reshaped_df.java)
# plot the chart python in the same java plot
plt.plot(reshaped_df.index, reshaped_df.python)
# and if we wanted plot all programming language in the DF in the same chart?
# using a for loop
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             # add legend (label for each line)
             linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

# ok our chart is ready but, be quite noisy
# so get smoothing by taking an average using the rolling mean
# in a window of time, so we use the pandas rolling() and mean() methods
# using a windows time average of 6
roll_df = reshaped_df.rolling(window=6).mean()

# plot parameters
plt.figure(figsize=(16,10))
#resizing fonts
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# add labels axis
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# add limit to y axis
plt.ylim(0, 35000)

# plot roll_df instead

for column in reshaped_df.columns:
  plt.plot(roll_df.index, roll_df[column],
  # add legend (label for each line)
          linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=16)
plt.show()
