from turtle import Turtle, Screen

x = Turtle()
x.shape("turtle")
x.color("MediumOrchid")

for _ in range(15):
    x.forward(10)
    x.penup()
    x.forward(10)
    x.pendown()


screen = Screen()
screen.exitonclick()