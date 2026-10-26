from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="make a guess", prompt="which turtle will win the race? please answer with 'red', 'orange', 'yellow', 'green', 'blue' or 'purple'.")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if guess:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == guess.lower():
                print(f"you've won. the {winner} turtle is the winner.")
            else:
                print(f"you've lost. the {winner} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# def forwards():
    # tim.forward(10)

# def backwards():
    # tim.backward(10)

# def counterclockwise():
    # tim.left(10)

# def clockwise():
    # tim.right(10)

# def clear():
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()

# screen.listen()
# screen.onkey(key="w", fun=forwards)
# screen.onkey(key="s", fun=backwards)
# screen.onkey(key="a", fun=counterclockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)
screen.exitonclick()