from turtle import Turtle, Screen

# my_turtle = Turtle()

# for i in range(4):
    # my_turtle.forward(100)
    # my_turtle.left(90)

dashed_line = Turtle()

for i in range(15):
    dashed_line.forward(10)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()

my_screen = Screen()
my_screen.exitonclick()