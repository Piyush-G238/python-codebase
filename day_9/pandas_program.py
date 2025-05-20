from pathlib import Path
import csv
import pandas
# from pandas import DataFrame

print(f"current directory: {Path.cwd()}")

data = pandas.read_csv('weather_data.csv')
print(type(data))

print(type(data["temp"]))

data_in_dictionary = data.to_dict()
print(data_in_dictionary)

temp_in_list = data['temp'].to_list()
print(temp_in_list)

# calculate average of temp
# panda approach
print(data['temp'].mean())
print(data['temp'].max())

average_temp = sum(temp_in_list) / len(temp_in_list)
print(average_temp)

print(data[data.day == "Monday"])

# data['temp'].max()
print(data[data['temp'] == data['temp'].max()])
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except ValueError as e:
#             print(f"error while parsing value: {e}")

# print(temperatures)