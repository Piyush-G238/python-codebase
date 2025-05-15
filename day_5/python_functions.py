# program 1
def greet(name = "David"):
    print(f"Hello, {name}")

greet("Emanuel")
greet()

# program 2
def add(num1, num2):
    return num1 + num2

print(add(3, 6))

# program 3
def square(num):
    return num ** 2

square(4)

# program 4
def is_odd_even(num):
    return num % 2 == 0

print(is_odd_even(7))
print(is_odd_even(10))

# program 5
def print_list(items):
    for item in items:
        print(item)

print_list(["Apple", "Banana", "Cherry"])

# program 6
def calculate(x, y):
    return x + y, x - y, x * y

a, b, c = calculate(10, 5)
print(a, b, c)

# program 7
def add_number(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_number(1,2, 4, 5))
print(add_number(1,2, 4, 5, 3, 6, 7))

# program 8 (keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(print_info(name = "Piyush the developer", age = 26, language = "Java"))
print(print_info(youtube_channel_name="Piyush The Developer", subscribers = 15, owner = "Piyush Gupta"))