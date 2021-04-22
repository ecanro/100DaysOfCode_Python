import pandas as pd
import matplotlib.pyplot as plt

'''
Challenge:

What are the shapes of the dataframes?
How many rows and columns?
What are the column names?
Complete the f-string to show the largest/smallest number in the search data column
Try the .describe() function to see some useful descriptive statistics
What is the periodicity of the time series data (daily, weekly, monthly)?
What does a value of 100 in the Google Trend search popularity actually mean?
'''


# TESLA DATA
df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
#shape
print(df_tesla.shape)
#head
print(df_tesla.head())
# using f-string
print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')
# describe with ()
print(df_tesla.describe())
# find missing values NaN (return true or false)
print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')  # -> False
# if is True get the number of missing values
print(f'The number of missing values for BTC Search?: {df_tesla.isna().values.sum()}')  # -> 0
# describe without () is how using head and tile at same time and shape
print(df_tesla.describe)

# UNEMPLOYMENT DATA
df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')
# shape
print(df_unemployment.shape)
# head and tail
print(df_unemployment.head())
print(df_unemployment.tail())
# using f-string
print(f'Largest value for UE_BENEFITS in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')
print(f'Smallest value for UE_BENEFITS in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.min()}')
# describe with ()
print(df_unemployment.describe())
# find missing values NaN (return true or false)
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')  # -> False
# if is True get the number of missing values
print(f'The number of missing values for UE_BENEFITS Search?: {df_unemployment.isna().values.sum()}')  # -> 0
# describe without () is how using head and tile at same time and shape
print(df_unemployment.describe)

# BITCOIN NEWS DATA
df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
# shape
print(df_btc_search.shape)
# head and tail
print(df_btc_search.head())
print(df_btc_search.tail())
# using f-string
print(f'Largest value for BITCOIN in News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}')
print(f'Smallest value for BITCOIN in News Search: {df_btc_search.BTC_NEWS_SEARCH.min()}')
# describe with ()
print(df_btc_search.describe())
# find missing values NaN (return true or false)
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
# get the number of missing values
print(f'The number of missing values for BTC Search?: {df_btc_search.isna().values.sum()}')  # -> 0
# describe without () is how using head and tile at same time and shape
print(df_btc_search.describe)

# BITCOIN PRICE DATA
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
# shape
print(df_btc_price.shape)
# head and tail
print(df_btc_price.head())
print(df_btc_price.tail())
# using f-string
print(f'Largest value for BITCOIN CLOSE: {df_btc_price.CLOSE.max()}')
print(f'Smallest value for BITCOIN CLOSE: {df_btc_price.CLOSE.min()}')
# describe with ()
print(df_btc_price.describe())
# find missing values NaN (return true or false)
print(f'Missing values for BTC Search?: {df_btc_price.isna().values.any()}')  # -> True
# if is True get the number of missing values
print(f'The number of missing values for BTC Search?: {df_btc_price.isna().values.sum()}')  # -> 2
# CLEAN DATA removing missing values
df_btc_price.dropna(inplace=True)
# describe without () is how using head and tile at same time and shape, but only work before use dropna
# print(df_btc_price.describe)


# Convert all DF time-series to Datetime
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
type(df_btc_price.DATE[0])
type(df_tesla.MONTH[0])

# RESAMPLING
# our BITCOIN Price is daily data, but our BITCOIN Search is monthly data
# we will convert our daily data to monthly
'''
To convert our daily data into monthly data, we're going to use the .resample() function. 
The only things we need to specify is which column to use (i.e., our DATE column) 
and what kind of sample frequency we want (i.e., the "rule"). We want a monthly frequency, 
so we use 'M'.  If you ever need to resample a time series to a different frequency, 
you can find a list of different options here (for example 'Y' for yearly or 'T' for minute).
'''
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
print(df_btc_monthly.head())
# if we wants the average
df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()
print(df_btc_monthly.head())