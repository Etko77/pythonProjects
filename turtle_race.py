import random
from turtle import Turtle,Screen

my_screen = Screen()

my_screen.setup(500, 400)
race_q = my_screen.textinput("Make your bet",
                             "Which turtle is gonna finish first?")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_list = []
condition = True
needed_y_value = -200
for c in colors:
    new_t = Turtle(shape="turtle")
    new_t.color(c)
    new_t.penup()
    new_t.goto(-230, needed_y_value + 50)
    needed_y_value += 50
    turtle_list.append(new_t)

while condition:
    for turtl in turtle_list:
        turtl.forward(random.randint(0, 10))
        (x, y) = turtl.position()
        if x >= 250:
            my_screen.title("Race is over!")
            if race_q == turtl.fillcolor():
                print(f"You've won the bet! {turtl.fillcolor()} has won!")
            else:
                print(f"You've lost the bet! {turtl.fillcolor()} has won!")
            condition = False

my_screen.exitonclick()