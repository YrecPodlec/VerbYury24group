
from turtle import *
import turtle as t

t.speed(0)
t.screensize(500, 500)
t.pensize(2)
t.home()
t.seth(0)
t.pd()
t.color('black')
t.circle(20, 80)
t.circle(200, 30)
t.circle(30, 60)
t.circle(200, 29.5)
t.color('black')
t.circle(20, 60)
t.circle(-150, 22)
t.circle(-50, 10)
t.circle(50, 70)
x_nose = t.xcor()
y_nose = t.ycor()
t.circle(30, 62)
t.circle(200, 15)
t.pu()
t.goto(x_nose, y_nose + 25)
t.seth(90)
t.pd()
t.begin_fill()
t.circle(8)
t.end_fill()
t.pu()
t.goto(x_nose + 48, y_nose + 55)
t.seth(90)
t.pd()
t.begin_fill()
t.circle(8)
t.end_fill()
t.pu()
t.color('#444444')
t.goto(x_nose + 100, y_nose + 110)
t.seth(182)
t.pd()
t.circle(15, 45)
t.color('black')
t.circle(10, 15)
t.circle(90, 70)
t.circle(25, 110)
t.rt(4)
t.circle(90, 70)
t.circle(10, 15)
t.color('#444444')
t.circle(15, 45)
t.pu()
t.color('black')
t.goto(x_nose + 90, y_nose - 30)
t.seth(-130)
t.pd()
t.circle(250, 28)
t.circle(10, 140)
t.circle(-250, 25)
t.circle(-200, 25)
t.circle(-50, 85) 
t.circle(8, 145)
t.circle(90, 45)
t.circle(550, 5)

t.seth(0)
t.circle(60, 85)
t.circle(40, 65)
t.circle(40, 60)
t.lt(150)
t.circle(-40, 90)
t.circle(-25, 100)
t.lt(5)
t.fd(20)
t.circle(10, 60)

t.rt(80)
t.circle(200, 35)

t.pensize(20)
t.color('#F03C3F')
t.lt(10)
t.circle(-200, 25)

t.pensize(2)
t.pu()
t.color('black')
t.goto(x_nose + 100, y_nose - 125)
t.pd()
t.seth(-50)
t.fd(25)
t.circle(10, 150)
t.fd(25)

t.pensize(2)
t.pu()
t.goto(x_nose + 314, y_nose - 125)
t.pd()
t.seth(-95)
t.fd(25)
t.circle(-5, 150)
t.fd(2)
t.hideturtle()
t.done()