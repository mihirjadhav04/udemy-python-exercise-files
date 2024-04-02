# # Working with csv files in python

# #! METHOD 1:
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)


# #! METHOD 2:
# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         # print(row)
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# #! METHOD 3:
# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# # print(data.to_dict)
# # temp_list = data["temp"].to_list()
# # print(temp_list)


# # print(data["temp"].mean())


# # Get data in Column
# # print(data["condition"])
# # print(data.condition)


# # Get data in Row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])


# # monday = data[data.day == "Monday"]
# # print(monday.condition)


# # Create a dataframe from scratch
# data_dict = {"students": ["Mihir", "Bhavin", "Shani"], "scores": [89, 78, 65]}
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("data_dict.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
