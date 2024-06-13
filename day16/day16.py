import turtle
import prettytable
timmy = turtle.Turtle()
timmy.color("blue")
timmy.shape("turtle")

for x in range(10):
    timmy.forward(200)
    timmy.back(200)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


table = prettytable.PrettyTable()
table.add_column("Pokemon_name",["Pikachu","Charmander","Squirtle"])
print(table)
