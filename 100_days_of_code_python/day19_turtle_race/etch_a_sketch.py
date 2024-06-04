from turtle import Turtle, Screen
x = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    x.forward(10)


def move_backwards():
    x.backward(10)


def turn_left():
    x.left(10)


def turn_right():
    x.right(10)


def clear():
    x.clear()
    x.penup()
    x.home()
    x.pendown()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()