# conditional statements in python
# conditional statements are essentials for controlling flow in python.

# basic structure - if, else and elif

# program_1
age = 18
if age < 18:
    print("You are not eligible for driving vehicles")
else:
    print("Your are eligible for driving vehicles")

# program_2
num = 5
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#program_3
print("Welcome to rollercoaster ride!")
height_in_cms = int(input("What's your height (in cms)? "))
if height_in_cms < 120:
    print("Sorry! You can't ride on roller coaster")
else:
    print("Yes! You can ride on roller coaster")
    
# Nested if statements
print("Welcome to amazing rollercoaster!")
customer_height = int(input("What's your height (in cms)?"))
customer_age = int(input("What's your age?"))
want_photos = input("Do you want photos?")

total_fare = 0
if customer_height > 120:
    print("Yes! you can ride on rollercoaster")
    if customer_age < 12:
        total_fare = 5
    elif customer_age > 12 and customer_age <= 18:
        total_fare = 7
    else:
        total_fare = 12
    
    if want_photos == "Yes":
        total_fare += 3
    print(f"The Total amount is: ${total_fare}")
else:
    print("Sorry! You cannot ride on rollercoaster")

# program 4
print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size of pizza do you want? S, M or L: ")
want_pepperoni = input("Do you want pepperoni on your pizza?: ")
want_extra_cheese = input("Do you want extra cheese on your pizza?: ")

total_amount = 0
if pizza_size == "S":
    total_amount = 15
elif pizza_size == "M":
    total_amount = 20
else:
    total_amount = 25

if want_pepperoni == "Yes":
    total_amount += 2
if want_extra_cheese == "Yes":
    total_amount += 2

print(f"Your total amount for pizza: ${total_amount}")