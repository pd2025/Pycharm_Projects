import turtle
turtle = turtle.Turtle()

p = 0
def squares():
    for i in range (4):
        turtle.fd(20)
        turtle.lt(90)
    turtle.pu()
    turtle.fd(30)
    turtle.pd()
    turtle.lt(90)
    turtle.fd(30)
    turtle.lt(90)
    turtle.fd(40)
    turtle.lt(90)
    turtle.fd(40)
    turtle.lt(90)
    turtle.fd(40)
    turtle.lt(90)
    turtle.fd(10)
    # new square
    turtle.pu()
    turtle.fd(40)
    turtle.pd()
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(60)
    turtle.lt(90)
    turtle.fd(60)
    turtle.lt(90)
    turtle.fd(60)
    turtle.lt(90)
    turtle.fd(20)



squares()