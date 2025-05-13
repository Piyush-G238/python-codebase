print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill (in $)?: "))
tip_amount = int(input("How much tip would you like to give? 10, 12 or 15: "))
no_of_people = int(input("How many people want to split the amount?: "))

total_amount = total_bill + tip_amount
tip_per_person = total_amount / no_of_people

print(f"Each person has to pay ${tip_per_person}")
