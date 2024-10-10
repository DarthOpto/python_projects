import turtle as t
import random
x = t.Turtle()
x.shape("turtle")
x.color("MediumOrchid")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
x.pensize(15)
x.speed("fastest")

for _ in range(1000):
    x.color(random_color())
    x.forward(30)
    x.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()