import pandas as pd
import matplotlib.pyplot as plt

#using Locators and DateFormatters to generate Tick Marks on a Time Line
import matplotlib.dates as mdates

df_unemployed = pd.read_csv('./data/UE Benefits Search vs UE Rate 2004-19.csv')

# Calculate the rolling average over a 6 month window
df_rolling = df_unemployed[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
# number of row and columns
df_unemployed.shape
# print the general view
df_unemployed.head()
print(f"'Largest value for 'Unemployed Benefits' in Web Search: {df_unemployed.UE_BENEFITS_WEB_SEARCH.max()}")

print(f"NAN values in U/E DF:? {df_unemployed.isna().values.any()}")

#DATETIME data
df_unemployed.MONTH = pd.to_datetime(df_unemployed.MONTH)


#Data Visualization with matplolib
#Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes.

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
#use Grids
plt.grid(color='grey', linestyle='--', linewidth=0.5)

ax1 = plt.gca()
# ax1.grid(color='grey', linestyle='--')
ax2 = plt.twinx()


# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('FRED U/E Rate', color="#1C86EE", fontsize=14)
ax2.set_ylabel('Search trend', color="#FF4500", fontsize=14)


#create locators for tick marks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# format the ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)


# Set the minimum and maximum values on the axes
ax1.set_ylim(bottom=0, top=10.5)
ax1.set_xlim([df_unemployed.MONTH.min(), df_unemployed.MONTH.max()])


ax1.plot(df_unemployed.MONTH, df_unemployed.UNRATE, color='#E6232E', linewidth=3, linestyle='--')#using HEX color code
ax2.plot(df_unemployed.MONTH, df_unemployed.UE_BENEFITS_WEB_SEARCH, color='blue', linewidth=3)

# Displays chart explicitly
plt.show()


ax1.plot(df_unemployed.MONTH, df_rolling.UNRATE, 'purple', linewidth=3, linestyle='-.')
ax2.plot(df_unemployed.MONTH, df_rolling.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()






