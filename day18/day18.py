import random
import turtle
from turtle import Turtle, Screen
from random import Random

rafael = Turtle()
rafael.shape("circle")
rafael.color("green")
my_screen = Screen()

my_screen.colormode(255)
# for i in range(6):
#     if i % 2 == 0:
#         rafael.penup()
#     else:
#         rafael.pendown()
#
#     rafael.forward(100)
#
#     rafael.left(60)

angles = 3
# for i in range(10):
#     for j in range(angles):
#         rafael.forward(100)
#         rafael.left(360 / angles)
#     angles+=1

rafael.speed(0)
rafael.width(10)


def random_color_pick():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def spirograph():
    rafael.width(1)
    for i in range(180):
        rafael.color(random_color_pick())
        rafael.circle(100)
        rafael.left(2)


spirograph()

rafael.width(5)
for i in range(200):

    rafael.color(random_color_pick())

    num = random.randint(1, 4)
    l_or_r = random.randint(1, 2)

    if num == 1:
        rafael.forward(40)
    elif num == 2:
        rafael.backward(40)
    elif num == 3:
        rafael.left(90)
        if l_or_r == 1:
            rafael.backward(40)
        elif l_or_r == 2:
            rafael.forward(40)
    elif num == 5:
        rafael.right(90)
        if l_or_r == 1:
            rafael.backward(40)
        elif l_or_r == 2:
            rafael.forward(40)
