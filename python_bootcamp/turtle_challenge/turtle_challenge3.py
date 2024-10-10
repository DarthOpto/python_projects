from turtle import Turtle, Screen
import random

x = Turtle()
x.shape("turtle")
x.color("MediumOrchid")

colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        x.forward(100)
        x.right(angle)


for shape_side_n in range(3, 11):
    x.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()