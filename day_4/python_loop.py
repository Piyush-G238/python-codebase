# program 1
fruits = ("Apple", "Banana", "Cherry")
for fruit in fruits:
    print(fruit)

# program 2
for i in range(5): # 0 to n-1
    print(i)

key_value_pair = {"name": "piyush", "designation": "engineer"}
for k,v in key_value_pair.items():
    print(f"{k} : {v}")

# program 3
student_scores = [68, 78, 49, 120, 113, 184, 24, 59, 68, 199, 65, 89]
total_score = 0
max_score = 0
for score in student_scores:
    total_score += score
    if score > max_score:
        max_score = score

print(f"Total score: {total_score}")
print(f"Average score: {total_score / len(student_scores)}")
print(f"Max score in the list: {max_score}")

# program 4
j = 0
while j <= 5:
    print(j)
    j += 1