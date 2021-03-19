# TODO: working with cvs files
"""basics and low functional"""
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data_file)

"""using csv module"""
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

"""using pandas package"""
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
# average = sum(temp_list) /len(temp_list)
# print(average)

# we can use bracket notation o dot notation

# working with columns->ez
print(data["temp"].mean())
print(data["temp"].max())
print(data.day)

# working with rows->all pandas are case sensitive
print(data[data.day == "Monday"])

# print the day with max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(f" Monday condition = {monday.condition}")

# temp to farenheit
temp_fahrenheit = data.temp * 9 / 5 + 32
print(temp_fahrenheit)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Jhon", "Edgar"],
    "scores": [76, 80, 85]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")