from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

#for i in range(47):
#    t.pendown()
#    t.forward(10)
#    t.penup()
#    t.forward(10)

number = 3

# t.penup()
# t.left(90)
# t.forward(250)
# t.right(90)
# t.pendown()

screen.colormode(255)
screen.setup(800, 600)

for j in range(9):
    cur_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.color(cur_color)
    for i in range(number):
        t.forward(75)
        t.right(360 / number)
        t.forward(75)
    number += 1

print(screen.canvheight)
screen.exitonclick()
