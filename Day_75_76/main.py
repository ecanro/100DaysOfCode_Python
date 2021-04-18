import pandas as pd
import matplotlib.pyplot as plt
'''
Introduction
Today we'll dive deep into a dataset all about LEGO. From the dataset we can ask whole bunch of interesting questions about the history of the LEGO company, their product offering, and which LEGO set ultimately rules them all:

What is the most enormous LEGO set ever created and how many parts did it have?
How did the LEGO company start out? In which year were the first LEGO sets released and how many sets did the company sell when it first launched?
Which LEGO theme has the most sets? Is it one of LEGO's own themes like Ninjago or a theme they licensed liked Harry Potter or Marvel Superheroes?
When did the LEGO company really expand its product offering? Can we spot a change in the company strategy based on how many themes and sets did it released year-on-year?
Did LEGO sets grow in size and complexity over time? Do older LEGO sets tend to have more or fewer parts than newer sets?
Data Source

Rebrickable has compiled data on all the LEGO pieces in existence. I recommend you use download the .csv files provided in this lesson.
'''

colors = pd.read_csv('data/colors.csv')
print(colors.head())
# using dot notation
print(colors.name.nunique())

colors.groupby('is_trans').count()

colors.is_trans.value_counts()

sets = pd.read_csv('data/sets.csv')
print(sets.head())
print(sets.tail())
sets.sort_values('year').head()
sets[sets.year == 1949]
sets.sort_values('num_parts', ascending=False).head()
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()
sets_by_year['set_num'].tail()

#Using Matplotlib
# resizing chart
plt.figure(figsize=(16,10))
#resizing fonts
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# add labels axis
plt.xlabel('Year', fontsize=14)
plt.ylabel('Sets', fontsize=14)
# add limit to y axis
#plt.ylim(0, 800)
# plot the chart sets
#plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
plt.show()

themes_by_year = sets.groupby('year').agg({'theme_id':pd.Series.nunique})
themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)
themes_by_year.head()
themes_by_year.tail()

#Using Matplotlib
# resizing chart
plt.figure(figsize=(16,10))
#resizing fonts
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# add labels axis
plt.xlabel('Year', fontsize=14)
plt.ylabel('Themes', fontsize=14)
# add limit to y axis
#plt.ylim(0, 800)
# plot the chart sets
#plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
plt.show()

# Two Separate Axes
ax1 = plt.gca() # get current axes
ax2 = ax1.twinx()
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of sets', color='green')
ax2.set_ylabel('Number of themes', color='blue')
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], 'g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], 'b')
plt.show()

avg_parts_set = sets.groupby('year').agg({'num_parts': pd.Series.nunique})
avg_parts_set.rename(columns={'num_parts':'average'}, inplace=True)
avg_parts_set.head()
avg_parts_set.tail()

plt.scatter(avg_parts_set.index[:-2], avg_parts_set.average[:-2])

set_theme_count = sets['theme_id'].value_counts()
print(set_theme_count[:5])

themes = pd.read_csv('data/themes.csv')
themes.head()

print(themes[themes.name == 'Star Wars'])

print(sets[sets.theme_id == 209])
print(sets[sets.theme_id == 158])


# convert pandas series into a pandas df
set_theme_count = pd.DataFrame({'id':set_theme_count.index, 'set_count':set_theme_count.values})
set_theme_count.head()

merge_df = pd.merge(set_theme_count, themes, on='id')
print(merge_df[:3])

plt.bar(merge_df.name[:10], merge_df.set_count[:10])
plt.show()