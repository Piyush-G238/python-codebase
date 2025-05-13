# variable and data type in python

# variables
# Reference for value in memory, python is dynamically typed (don't need to specify data type of variable)

name = input("please enter your name:")
# "Piyush the developer"
age = 27
isActive = True

print(f"character length of name is: {len(name)}")
print(f"is piyush active: {isActive}")

# data types in python
# int
sprintWeek = 17

# float
workingDuration = 9.15

# str (string)
owner = "Piyush the developer"

# bool
isReady = True

# list - ordered and mutable collection
nums = [1, 2, 3]

# tuple - ordered and immutable collection
t = (1, 2)

# dict - key value pair (like hashmap)
developerRating = {"name": "Piyush the developer", "rating": 5.0}

# set - unordered collection having unique elements
s = {1, 2, 3}

# NoneType (equivalent to null)
x = None
print(type(x))

# print(len(12345)) - example of type error

myExperience = float("5.54")
print(myExperience)

isManager = bool("True")
print(f"{owner} is the Manager: {isManager}")

print(str(10 % 3))