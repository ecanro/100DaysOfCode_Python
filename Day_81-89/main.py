import pandas as pd
import matplotlib as plt

df_tesla = pd.read_csv('./data/TESLA Search Trend vs Price.csv')

print(f"General data: {df_tesla.head()}")
print(f"'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}")
print(f"'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}")
df_tesla.describe()

df_unemployed = pd.read_csv('./data/UE Benefits Search vs UE Rate 2004-19.csv')
# number of row and columns
df_unemployed.shape
# print the general view
df_unemployed.head()
print(f"'Largest value for 'Unemployed Benefits' in Web Search: {df_unemployed.UE_BENEFITS_WEB_SEARCH.max()}")

df_bitcoin = pd.read_csv('./data/Bitcoin Search Trend.csv')
df_bitcoin.shape
df_bitcoin.head()
#DATA CLEANING
#Verify if DF have NAN value
print(f"NAN values in Tesla DF:? {df_tesla.isna().values.any()}")
print(f"NAN values in U/E DF:? {df_unemployed.isna().values.any()}")
print(f"NAN values in Bitcoin DF:? {df_bitcoin.isna().values.any()}")

#Verify Daily Bitcoin price data
df_BTC_price = pd.read_csv('./data/Daily Bitcoin Price.csv')
print(f"missing values in Bitcoin price?: {df_BTC_price.isna().values.any()}")
#Get the total of missing values
print(f'Number of missing values: {df_BTC_price.isna().values.sum()}')
#or
df_BTC_price[df_BTC_price.CLOSE.isna()]
#now cleaning this NAN values
df_BTC_price = df_BTC_price.dropna()
#or more functional
df_BTC_price.dropna(inplace=True)

#Convert string into datetime
#firts check the data type
type(df_tesla.MONTH[0])

#DATETIME data
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployed.MONTH = pd.to_datetime(df_unemployed.MONTH)
df_bitcoin.MONTH = pd.to_datetime(df_bitcoin.MONTH)
df_BTC_price.DATE = pd.to_datetime(df_BTC_price.DATE)

df_tesla.MONTH.head()

#Resampling Time Series Data
#Daily data into Monthly data in bitcoin and btc data
#After resampling, we need to figure out how the data should be treated. In our case, we want the last available price of the month - the price at month-end.
df_btc_monthly = df_BTC_price.resample('M', on="DATE").last()
#If we wanted the average price over the course of the month, we could use something like:
df_btc_monthly = df_BTC_price.resample('M', on="DATE").mean()
print(df_btc_monthly.shape)
df_btc_monthly.head()

#Data Visualization with matplolib
#Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes.
ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_ylabel('TSLA Stock Price')
ax2.set_ylabel('Search trend')

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='green')



