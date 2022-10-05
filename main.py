# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# converting to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# sum_temp = 0
# for temp in temp_list:
#     sum_temp = sum_temp + temp
#
# avg = sum_temp/7
# print(avg)
#  OR
# print(data["temp"].mean())

# print(data["temp"].max())

#Get data in row
# print(data[data["day"]=="Monday"])

# Row of data which has the highest temperature
# max_temp = data["temp"].max()
# print(data[data["temp"]==max_temp])

# monday = data[data["day"]=="Monday"]
# print(monday["condition"])

# Converting Mondays temp to fahrenheit
# monday = data[data["day"]=="Monday"]
# monday_temp = monday["temp"]
# print(monday_temp*1.8+32)

# Create a dataframe from a scratch
# data_dict = {
#     "students":["Amy","James","Angela"],
#     "scores":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")