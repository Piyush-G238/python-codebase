# program for creating coffee machine (just for fun)

# Make 3 hot flavours - espresso, latte, cappuccino
# espresso - 50ml water, 18g coffee - $1.50
# latte - 200ml water, 24g coffee, 150ml milk - $2.50
# cappuccino - 250ml water, 24g coffee, 100ml milk - $3.00
# coin operated by coffee machine - penny=0.01, nickel=0.05, dime=0.1, quarter=0.25
# program requirement
# 1. print report - how much water, coffee left?
# 2. check resources sufficient for making coffee
# 3. Process coins

espresso = {
    "price": 1.50,
    "water": 50,
    "coffee": 18,
    "milk": 0
}

latte = {
    "price": 2.50,
    "water": 200,
    "coffee": 24,
    "milk": 150
}

cappuccino = {
    "price": 3.00,
    "water": 250,
    "coffee": 24,
    "milk": 100
}

coffee_machine = {
    "water": 1000,
    "milk": 500,
    "coffee": 500,
    "price": 0
}

def prepare_report():
    print(f"Water: {coffee_machine.get('water')}")
    print(f"Milk: {coffee_machine.get('milk')}")
    print(f"Coffee: {coffee_machine.get('coffee')}")
    print(f"Money: {coffee_machine.get('money')}")

def check_for_water(water_qty):
    if coffee_machine.get("water") < water_qty:
        print("Sorry there is not enough water")

def check_for_coffee(coffee_qty):
    if coffee_machine.get("coffee") < coffee_qty:
        print("Sorry there is not enough coffee")

def check_for_milk(milk_qty):
    if coffee_machine.get("milk") < milk_qty:
        print("Sorry there is not enough milk")

def ask_for_money(amount):
    penny_qty = int(input("Insert amount of penny: "))
    nickel_qty = int(input("Insert amount of nickel: "))
    dime_qty = int(input("Insert amount of dime: "))
    quarter_qty = int(input("Insert amount of quarter: "))

    total = ((penny_qty * 0.01) +
             (nickel_qty * 0.05) +
             (dime_qty * 0.1) +
             (quarter_qty * 0.25))
    if total < amount:
        print("Sorry that's not enough money. Money refunded.")

    return {
        "total" : total,
        "penny": penny_qty,
        "nickel": nickel_qty,
        "dime": dime_qty,
        "quarter": quarter_qty
    }

def process_coffee(
        water_amt,
        coffee_amt,
        milk_amt,
        price):

    remaining_coffee = coffee_machine.get("coffee") - coffee_amt
    remaining_water = coffee_machine.get("water") - water_amt
    remaining_milk = coffee_machine.get("milk") - milk_amt
    total_amount = coffee_machine.get("price") + price
    coffee_machine.update({
        "water": remaining_water,
        "money" : total_amount,
        "coffee": remaining_coffee,
        "milk" : remaining_milk
    })

while True:
    option_selected = input("What would you like? (espresso/latte/cappuccino): ")
    if option_selected == "report":
        prepare_report()

    elif option_selected == "espresso":
        check_for_water(espresso.get("water"))
        check_for_coffee(espresso.get("coffee"))
        money_processed = ask_for_money(espresso.get("price"))
        process_coffee(
            espresso.get("water"),
            espresso.get("coffee"),
            espresso.get("milk"),
            espresso.get("price"))
        print("Here is your espresso. Enjoy!")

    elif option_selected == "cappuccino":
        check_for_water(cappuccino.get("water"))
        check_for_coffee(cappuccino.get("coffee"))
        check_for_milk(cappuccino.get("milk"))
        money_processed = ask_for_money(cappuccino.get("price"))
        process_coffee(
            cappuccino.get("water"),
            cappuccino.get("coffee"),
            cappuccino.get("milk"),
            cappuccino.get("price"))
        print("Here is your cappuccino. Enjoy!")

    elif option_selected == "latte":
        check_for_water(latte.get("water"))
        check_for_coffee(latte.get("coffee"))
        check_for_milk(latte.get("milk"))
        money_processed = ask_for_money(latte.get("price"))
        process_coffee(
            latte.get("water"),
            latte.get("coffee"),
            latte.get("milk"),
            latte.get("price"))
        print("Here is your latte. Enjoy!")

    elif option_selected == "off":
        print("Thank you for using coffee machine!")
        break

    else:
        print("You have selected wrong option!")