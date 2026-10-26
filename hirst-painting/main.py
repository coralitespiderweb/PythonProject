import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

screen.colormode(255)
screen.setup(800, 600)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
    # r = color.rgb.r
    # g = color.rgb.g
    # b = color.rgb.b
    # new_color = (r, g, b)
    # rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(219, 207, 204), (209, 176, 130), (216, 203, 206), (162, 185, 194), (221, 195, 146), (204, 170, 182), (190, 199, 193), (174, 190, 175), (181, 197, 192), (202, 187, 184), (201, 185, 187), (201, 203, 210), (188, 190, 196), (189, 193, 194)]

def row():
    for i in range(9):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.dot(20, random.choice(color_list))
    if tim.xcor() == 450:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)

for x in range(10):
    row()

print(screen.canvheight)
screen.exitonclick()