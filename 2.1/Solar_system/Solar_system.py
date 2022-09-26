import turtle
import time
from math import *

win = turtle.Screen()
win.setup(1850, 950)
win.bgcolor('black')
win.tracer(0)

sun = turtle.Turtle()
sun.shape('circle')
sun.shapesize(5, 5)
sun.color('yellow')


class Planet(turtle.Turtle):
    def __init__(self, radius, color, size, star, line):
        super().__init__(shape='circle')
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.size = size
        self.shapesize(size, size)
        self.angle = 0
        self.star = star
        self.line = line

    def move(self):
        x = self.line + self.radius * cos(self.angle)
        y = self.radius * sin(self.angle) * 0.3

        self.goto(self.star.xcor() + x, self.star.ycor() + y)


earth = Planet(300, 'blue', 1, sun, 100)
mercury = Planet(110, 'grey', 0.6, sun, 0)
venus = Planet(180, 'orange', 0.8, sun, 50)
mars = Planet(400, 'red', 0.9, sun, 100)
jupyter = Planet(550, 'dark orange', 1.4, sun, 150)
saturn = Planet(670, 'gold', 1, sun, 170)

moon = Planet(40, 'grey', 0.2, earth, 0)
phobos = Planet(40, 'grey', 0.2, mars, 0)
deimos = Planet(35, 'white', 0.2, mars, 0)

myList = [mercury, venus, earth, moon, mars, phobos, deimos, jupyter, saturn]

for i in myList:
    i.penup()
    i.goto(i.radius + i.line, 0)
    if i.star == sun:
        i.pendown()

while True:
    win.update()
    for i in myList:
        i.move()

    moon.angle += 0.06
    phobos.angle += 0.06
    deimos.angle += 0.08

    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupyter.angle += 0.008
    saturn.angle += 0.006

    time.sleep(0.01)
