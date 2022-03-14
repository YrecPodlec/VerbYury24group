import turtle

square = turtle.Turtle()
square.shape("turtle")
for j in range(37):
    square.left(100)
    for i in range(3):
        square.forward(70)
        square.left(70)
turtle.exitonclick()