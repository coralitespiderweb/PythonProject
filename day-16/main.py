from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSlateGray3")
# timmy.forward(100)

# screen = Screen()
# screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Galarian Sirfetch'd", "Fighting"],
        ["Flying Pikachu VMax", "Electric"],
        ["Hisuasian Sneasel", "Dark"],
    ]
)
table.align = "l"
print(table)