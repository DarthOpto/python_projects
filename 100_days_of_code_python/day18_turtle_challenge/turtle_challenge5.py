import turtle as t
import random
x = t.Turtle()
x.shape("turtle")
x.color("MediumOrchid")
t.colormode(255)
x.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        x.color(random_color())
        x.circle(100)
        x.setheading(x.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()