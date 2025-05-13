# Quiz game with lifeline option

# Command line game that asks users multiple choice questions.
# Game tracks score of user and offer lifeline like 50-50/skip
# uses random module to pick question

import random

print("Welcome to the Python Quiz Game!")

quiz_questions = [
    (
        "What is the capital of France?", 
        ["Paris", "London", "Berlin", "Rome"], 
        "Paris"
    ),

    (
        "Which data type is immutable in Python?", 
        ["List", "Dictionary", "Tuple", "Set"], 
        "Tuple"
    ),

    (
        "What does the 'random.randint(1, 10)' function do?", 
        ["Returns a float between 1 and 10", 
        "Returns an integer from 1 to 10 (inclusive)", 
        "Generates a random list", 
        "Returns a string between 1 and 10"], 
        "Returns an integer from 1 to 10 (inclusive)"
    ),

    (
        "Which keyword is used for conditional branching in Python?", 
        ["if", "loop", "define", "function"], 
        "if"
    ),
    (
        "Which of the following is a valid Python set?", 
        ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "{\"1\": 2}"], 
        "{1, 2, 3}"
    ),
    (
        "What is the output of type(3.14)?", 
        ["int", "float", "str", "bool"], 
        "float"
    ),
    (
        "Which of these is used to add an element to a list?", 
        ["append()", "add()", "insert()", "extend()"], 
        "append()"
    ),
    (
        "What will be the result of 5 > 3 and 2 < 4?", 
        ["True", "False", "Error", "None"], 
        "True"
    ),
    (
        "How many elements are in the tuple: (1, 'a', 3.5)?", 
        ["1", "2", "3", "4"], 
        "3"
    ),
    (
        "Which function is used to shuffle a list randomly?", 
        ["random.shuffle()", "random.choice()", "random.sort()", "random.randomize()"], 
        "random.shuffle()"
    )
]

selected_ques = random.randint(0, len(quiz_questions) - 1)

print("Question")
print(quiz_questions[selected_ques][0])
print(f"a) {quiz_questions[selected_ques][1][0]}")
print(f"b) {quiz_questions[selected_ques][1][1]}")
print(f"c) {quiz_questions[selected_ques][1][2]}")
print(f"d) {quiz_questions[selected_ques][1][3]}")
answer = input("Type your answer or type 'lifeline' to use a lifeline: ")
correct_answer = quiz_questions[selected_ques][2]

if answer == "lifeline":
    lifeline = input("Do you want 50-50 or skip the question: ")
    if lifeline == "50-50":
        random_option = random.randint(0, 3)
        remaining_options = [quiz_questions[selected_ques][1][random_option], correct_answer]
        print(f"a) {remaining_options[0]}")
        print(f"b) {remaining_options[1]}")
        answer = input("Type your answer: ")
    else:
        print("Question is skipped")
else:
    if answer == correct_answer:
        print("Yes your answer is correct!")
    else:
        print(f"Oops, correct answer is: {correct_answer}")