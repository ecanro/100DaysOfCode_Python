import pandas as pd
import matplotlib.pyplot as plt
#using Locators and DateFormatters to generate Tick Marks on a Time Line
import matplotlib.dates as mdates


df_bitcoin = pd.read_csv('./data/Bitcoin Search Trend.csv')
df_bitcoin.shape
df_bitcoin.head()
#DATA CLEANING
#Verify if DF have NAN value
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

#DATETIME data
df_bitcoin.MONTH = pd.to_datetime(df_bitcoin.MONTH)
df_BTC_price.DATE = pd.to_datetime(df_BTC_price.DATE)

#Resampling Time Series Data
#Daily data into Monthly data in bitcoin and btc data
#After resampling, we need to figure out how the data should be treated. In our case, we want the last available price of the month - the price at month-end.
df_btc_monthly = df_BTC_price.resample('M', on="DATE").last()
#If we wanted the average price over the course of the month, we could use something like:
df_btc_monthly = df_BTC_price.resample('M', on="DATE").mean()
print(df_btc_monthly.shape)
df_btc_monthly.head()

#Data Visualization with matplolib
#Bitcoin: Line Style and Markers

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)


ax1 = plt.gca()
ax2 = plt.twinx()


# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('BTC Price', color="#1C86EE", fontsize=14)
ax2.set_ylabel('Search trend', color="#FF4500", fontsize=14)

#create locators for tick marks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 15000])
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])


ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color='#E6232E', linewidth=3, linestyle='--')#using HEX color code
ax2.plot(df_btc_monthly.index, df_bitcoin.BTC_NEWS_SEARCH, color='blue', linewidth=3, marker='o')

# Displays chart explicitly
plt.show()







