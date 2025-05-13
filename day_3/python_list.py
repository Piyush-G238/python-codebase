import random

# program 1
fruit_collection = [
    "Apple", 
    "Mango", 
    "Banana", 
    "Cherry", 
    "Strawberry"
]

vegetable_collection = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery"
]

states_of_america = [
    "California",
    "Nevada",
    "Pennsylvania",
    "Washington",
    "New Jersey"
]

print(fruit_collection[-1])
print(states_of_america[1])

states_of_america.append("New Delhi")
print(states_of_america)

# program 2
friend_list = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emanuel"
]

index = random.randint(0, len(friend_list))
print(friend_list[index])

# program 3 (nested list)
dirty_dozen = [
    fruit_collection,
    vegetable_collection
]

print(dirty_dozen)