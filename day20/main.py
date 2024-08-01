import time
from turtle import Turtle, Screen
from snake_movements import Snake

screen = Screen()
screen.setup(600, 600)
# screen.bgpic("Snake-cobra.gif")
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
the_snek = Snake()


game = True
while game:
    screen.update()
    the_snek.base_movement()
    

screen.exitonclick()