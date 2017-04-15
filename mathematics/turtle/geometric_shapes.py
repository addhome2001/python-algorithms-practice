import turtle

turtle.shape('turtle')
turtle.color('yellow')
turtle.fillcolor('white')
turtle.bgcolor('black')
turtle.pensize('2')

def circle(scale):
    turtle.down()
    turtle.begin_fill()
    unit = 360 / scale
    for i in range(unit):
        turtle.forward(scale)
        turtle.left(scale)
    turtle.end_fill()
    turtle.up()

def square():
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.left(90)
        turtle.forward(100)
    turtle.end_fill()
    turtle.up()

def triangle():
    turtle.down()
    turtle.begin_fill()
    for i in range(3):
        turtle.left(120)
        turtle.forward(120)
    turtle.end_fill()
    turtle.up()

circle(10)
turtle.goto(-150, 0)
square()
turtle.goto(250, 0)
triangle()

turtle.exitonclick()
