import turtle as tim
import random

t = tim.Turtle()
screen = tim.Screen()
tim.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# directions = [0, 90, 180, 270]
# t.pensize(15)
# move = 30
t.speed("fastest")
degree = 5

# for i in range(200):
    # t.color(random_color())
    # move = random.randint(20, 100)
    # t.forward(move)
    # t.setheading(random.choice(directions))

for i in range(int(360 / degree)):
    t.color(random_color())
    t.circle(100)
    t.right(degree)

print(screen.canvheight)
screen.exitonclick()