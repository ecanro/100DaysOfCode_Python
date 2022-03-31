'''
How to quickly remove duplicates

How to remove unwanted symbols and convert data into a numeric format

How to wrangle columns containing nested data with Pandas

How to create compelling data visualisations with the plotly library

Create vertical, horizontal and grouped bar charts

Create pie and donut charts for categorical data

Use colour scales to make beautiful scatter plots
'''

import pandas as pd

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

# Read the dataset
df = pd.read_csv('data/apps.csv')

# Data cleaning
print(df.head())
print(df.shape)
df.info()
print(df.sample(5))  # casi igual a shape

# Dropping Unused Columns and Removing NaN Values
df_clean = df.drop(columns=['Last_Updated', 'Android_Ver'])
df_clean.info()

df_clean = df_clean.dropna()
df_clean.info()
