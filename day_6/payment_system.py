from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def __init__(self, card_number):
        self.__card_number = card_number

    def pay(self, amount):
        print(f"Paid Rs.{amount} using credit card number ending with {self.__card_number}")

class UPI(Payment):
    def __init__(self, upi_id):
        self.__upi_id = upi_id

    def pay(self, amount):
        print(f"Paid Rs.{amount} using upi id: {self.__upi_id}")

class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__wallet = 0

    def add_money(self, amount):
        self.__wallet += amount
        print("amount added to wallet")

    def make_payment(self, method: Payment, amount):
        if self.__wallet < amount:
            print("Insufficient balance")
        else:
            self.__wallet -= amount
            method.pay(amount)
            print(f"Remaining balance: Rs.{self.__wallet}")

user = User("Mukesh", "mukesh@gmail.com")

upi = UPI("mukesh@ybl")
card = CreditCard("6799")

user.add_money(500)
user.make_payment(upi, 400)