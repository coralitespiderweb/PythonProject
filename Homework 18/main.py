from turtle import Turtle, Screen

conehead = Turtle()
conehead.shape("turtle")
# conehead.pendown()
conehead.color("black")
for _ in range(10):
    conehead.forward(10)
    conehead.pendown()
    conehead.forward(10)
    conehead.penup()
# conehead.forward(100)
#conehead.right(90)
#conehead.forward(100)
#conehead.right(90)
#conehead.forward(100)
#conehead.right(90)
#conehead.forward(100)

screen = Screen()
screen.exitonclick()