# exception handling in python

# program 1
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")

# program 2
try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("cleanup done ")

# program - 3 raising exceptions
def withdraw(balance, amount = 500):
    if balance < amount:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    new_balance = withdraw(5000, 6000)
except ValueError as e:
    print(f"Transaction failed: {e}")

# program 4 - creating your own exception and raising it
class NegativeValueError(Exception):
    def __init__(self, message):
        super().__init__(message)

def set_age(age):
    if age < 0:
        raise NegativeValueError("Age cannot be negative")

try:
    set_age(-8)
except NegativeValueError as e:
    print(f"Failed to set age: {e}")