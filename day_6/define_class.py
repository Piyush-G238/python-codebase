# OOP - a paradigm that allows you to structure your code using classes and objects.
# self - refers to instance of class, required in method definition to access instance variables.

# from turtle import Turtle

# Program 1 - defining a class and object

from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# new_turtle = Turtle()
# new_turtle.shape("turtle")
# new_turtle.color("green")
# new_turtle.forward(100)
# new_turtle.back(20)
# print(new_turtle)

# my_screen = Screen()
# my_screen.exitonclick()

hari = Person("Hari prasad", 27)
piyush = Person("Piyush The Developer", 27)

hari.greet()
piyush.greet()

# Program 2 - encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

bank_account = BankAccount(4000)
print(f"Current balance: {bank_account.get_balance()}")
bank_account.deposit(1000)
bank_account.withdraw(550)
print(f"Current balance: {bank_account.get_balance()}")

# Program 3 - Inheritance
class Employee:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.__department = department

    def get_department(self):
        return self.__department

deepak_dhyani = Manager("Deepak Dhyani", "HRIS")
piyush_the_developer = Employee("Piyush Gupta")

#Program 4 - Abstraction
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.drive()

# Use case of pass keyword
# The pass keyword in Python is a placeholder
# — it’s used when a statement is syntactically required but you don’t want to write any code yet.