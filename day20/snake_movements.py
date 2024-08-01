from turtle import Turtle
import time

def make_snake():
    the_snake = []
    starting_x = 0
    for i in range(0, 3):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(starting_x, 0)
        starting_x -= 20
        the_snake.append(snake_part)
    return the_snake


class Snake:
    def __init__(self):
        self.the_snake = make_snake()

    def base_movement(self):
        for i in range(len(self.the_snake) - 1, 0, -1):
            (x, y) = self.the_snake[i - 1].pos()
            self.the_snake[i].goto(x, y)
            time.sleep(1)
        self.the_snake[0].forward(20)
