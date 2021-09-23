import turtle
turtle = turtle.Turtle()

def squares (n):
    for i in range (n):
        for t in range (4):
            turtle.fd(20)
            turtle.lt(90)
        turtle.pu()
        turtle.fd(40)
        turtle.pd()

squares(5)
