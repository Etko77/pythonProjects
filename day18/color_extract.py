import random
import colorgram
import turtle as t_module

t_module.colormode(255)
tim = t_module.Turtle()
tim.speed(10)
tim.penup()
tim.hideturtle()
colors = colorgram.extract('hirst_painting.jpg', 10)
colors_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_c = (r, g, b)
    colors_list.append(new_c)
print(colors_list)
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
for i in range(1, len(colors_list)*10):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


my_screen = t_module.Screen()
my_screen.exitonclick()

