import pandas as pd

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