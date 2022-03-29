import pandas as pd
import matplotlib.pyplot as plt

#using Locators and DateFormatters to generate Tick Marks on a Time Line
import matplotlib.dates as mdates

df_tesla = pd.read_csv('./data/TESLA Search Trend vs Price.csv')

print(f"General data: {df_tesla.head()}")
print(f"'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}")
print(f"'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}")
df_tesla.describe()

#Convert string into datetime
#firts check the data type
type(df_tesla.MONTH[0])

#DATETIME data
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_tesla.MONTH.head()


#Data Visualization with matplolib
#Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes.

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = plt.twinx()


# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('TSLA Stock Price', color="#1C86EE", fontsize=14)
ax2.set_ylabel('Search trend', color="#FF4500", fontsize=14)
ax1.set_xlabel("Year", fontsize=14)


# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

#create locators for tick marks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# format the ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)#using HEX color code
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='blue', linewidth=3)

# Displays chart explicitly
plt.show()