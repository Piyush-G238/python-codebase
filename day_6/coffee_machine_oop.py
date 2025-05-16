# coffee machine program using oop

class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.money = 0

    def generate_report(self):
        print(f"""
        Water: {self.water}
        Milk: {self.milk}
        Coffee: {self.coffee}
        Money: ${self.money}
        """)

    def check_for_resource(self):
        pass

    def prepare_coffee(self):
        pass

    def process_transaction(self):
        pass

class Coffee:
    def __init__(self, water, coffee, milk, price):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.price = price

