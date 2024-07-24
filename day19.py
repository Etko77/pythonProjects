import turtle as turtle_module

arrow = turtle_module.Turtle()
my_screen = turtle_module.Screen()


def move_forward():
    arrow.forward(10)


def move_backward():
    arrow.backward(10)


def turn_left():
    arrow.left(10)


def turn_right():
    arrow.right(10)


def clear_screen():
    arrow.clear()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="c", fun=clear_screen)
my_screen.exitonclick()
