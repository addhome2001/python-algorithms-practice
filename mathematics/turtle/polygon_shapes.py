import turtle

turtle.shape('turtle')
turtle.color('yellow')
turtle.fillcolor('white')
turtle.bgcolor('black')
turtle.pensize('2')

def polygon(length, num):
    angle = 360 / num
    turtle.down()
    turtle.begin_fill()
    for i in range(num):
        turtle.left(angle)
        turtle.forward(length)
    turtle.end_fill()
    turtle.up()

polygon(80, 8)

turtle.exitonclick()
