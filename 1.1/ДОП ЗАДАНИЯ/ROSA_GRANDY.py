from turtle import Turtle, Screen
from math import pi, sin, cos
screen = Screen()
turtle = Turtle()
turtle.pencolor('purple')
turtle.speed(0)
radius = 100
parts = 9
for angle in range(500):
    formula = radius*sin(parts*angle)
    x = formula*cos(angle)
    y = formula*sin(angle)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.dot()
screen.exitonclick()
