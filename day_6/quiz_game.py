class Question:
    def __init__(self, text, answer):
        self.__text = text
        self.__answer = answer

    def get_text(self):
        return self.__text

    def get_answer(self):
        return self.__answer


class QuizBrain:
    def __init__(self, question_list):
        self.__question_list = question_list
        self.__ques_no = 0
        self.__current_score = 0

    def next_question(self):
        ques = f"{self.__ques_no}. {self.__question_list[self.__ques_no]} (True/False): "
        self.__ques_no += 1
        return ques

    def check_answer(self, user_ans):
        curr_ques = self.__question_list[self.__ques_no]
        if curr_ques.answer == user_ans:
            self.__current_score += 1
            print("You got it correct!")
        else:
            print("Sorry, wrong answer!")
        print(f"Your current score: {self.__current_score}")
        # pass

# main code
question_bank = [
    Question("The Earth revolves around the Sun.", True),
    Question("Sound travels faster than light.", False),
    Question("Water boils at 100 degrees Celsius at standard atmospheric pressure.", True),
    Question("The Great Wall of China is visible from the Moon with the naked eye.", False),
    Question("Python is a high-level programming language.", True),
    Question("Humans have more than two lungs.", False),
    Question("Light travels in a straight line.", True),
    Question("Sharks are mammals.", False),
    Question("The chemical symbol for gold is Au.", True),
    Question("Venus is the closest planet to the Sun.", False)
]
quiz_brain = QuizBrain(question_bank)

idx = 0
while idx < len(question_bank):
    typed_value = input(quiz_brain.next_question())
    user_answer = bool(typed_value)
    quiz_brain.check_answer(user_answer)

