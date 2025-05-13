import random
import my_module

random_int = random.randint(1, 10) # generating random integer btw 1,10

print(random_int)
print(my_module.my_favourite_number)

random_float = random.random() #generate a random float between 0 to 1

# generating random number between two numbers
random_float_2 = random.uniform(2, 3)
print(random_float)
print(random_float_2)