import turtle
import pandas

screen = turtle.Screen()
picture = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)

picture.shape(image)
picture.color("black")
picture.penup()

scribe = turtle.Turtle()
scribe.penup()
scribe.hideturtle()

data = pandas.read_csv("50_states.csv")
correct_guesses = []
states = []
answer_state = ""

while len(correct_guesses) < 50:
    if answer_state.title() == "Exit":
        missing_states = [state for state in states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    elif len(correct_guesses) == 0:
        answer_state = screen.textinput(title="Guess The State", prompt="What's another state name?").title()

    else:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state name?").title()

    for line in data.state:
        states = data.state.to_list()




## print(data[data.state == answer_state].x)
## print(data[data.state == answer_state].y)

    if answer_state in states:
        scribe.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        scribe.write(answer_state, align="center", font=("Arial", 11, "normal"))
        correct_guesses.append(answer_state)



turtle.exitonclick()