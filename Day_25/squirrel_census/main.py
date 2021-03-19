# TODO: using the csv data create a new csv with all the fur color and qty.

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = (data["Primary Fur Color"])
#print(fur_colors)
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
#print(black_squirrels)
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
#print(cinnamon_squirrels)
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
#print(gray_squirrels)

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [ black_squirrels, cinnamon_squirrels, gray_squirrels]
}
#print(data_dict)
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_fur_colors_count.csv")