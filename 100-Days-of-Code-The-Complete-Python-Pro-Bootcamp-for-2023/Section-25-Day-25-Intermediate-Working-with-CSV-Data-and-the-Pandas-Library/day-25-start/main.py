import pandas as pd
# TODO get every color type and create a new data_dict
#  than convert to pandas.to_csv with color and the sum of each color
#  add two columns names
data_file = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
var = pd.Series(data_file["Primary Fur Color"])
color_list = list(var.values)
color_dict = {}

for i in range(len(color_list)):
    # if i != 0:
        if  color_list[i] not in color_dict:
            color_dict[color_list[i]] = 1
        else:
            color_dict[color_list[i]] += 1

new_color_table = pd.DataFrame(color_dict.items(), columns=["Color", "Count"])
new_color_table.to_csv("Squirrels_colors_count.csv")

with open("Squirrels_colors_count.csv") as file:
    print(file.read())

# for color in color_list:
print(color_list.count("Gray"))
###
###
###
###
###

import pandas

# Create your own DataFrame and convert to csv
data_dict = {
    "students": ["Anny", "Neuro", "Vedal"],
    "scores": [69, 100, 91]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
with open("new_data.csv") as student_score:
    print(student_score.read())

#


#find in the row the max num and convert to Fahrenheit
#F = C * 9/5 + 32     Fahrenheit Formula
data = pandas.read_csv("weather_data.csv")
print(data.loc(1)["temp"].max() * 9/5 + 32)

###
#find temp from monday and their Fahrenheit
data = pandas.read_csv("weather_data.csv")
monday = data.loc[data.day == "Monday", "temp"].iloc[0]
print(monday * 9/5 + 32)

###

#get a row from a data table | the row with max number
data = pandas.read_csv("weather_data.csv")
print(data[data.temp == data.temp.max()].temp.values[0])

###

#get max and min temperature
data = pandas.read_csv("weather_data.csv")
print(data["temp"].max(), "|", data["temp"].min())

###

#get average / mean of column "temp"
data = pandas.read_csv("weather_data.csv")
print(round(data["temp"].mean(), 2))

###

#get average / mean of column "temp"
data = pandas.read_csv("weather_data.csv")
average_temp = pandas.Series(data["temp"])
print(round(average_temp.mean(), 2))

###

#get average / mean of column "temp"
temperature = data["temp"].to_list()
sum_temperatures = 0
for i in temperature:
    sum_temperatures += i
average_temperature = round(sum_temperatures / len(temperature), 2)
print(average_temperature)

###
###
###
###
###

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     data = [data.strip() for data in data]
#     print(data)

###

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if  str.isnumeric(row[1]):
#             temperatures.append(int(row[1]))
#         else:
#             temperatures.append(row[1])
#         print(row)
#     print(temperatures)
#