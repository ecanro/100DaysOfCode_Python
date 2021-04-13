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