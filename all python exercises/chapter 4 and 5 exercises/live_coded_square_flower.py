import turtle
t = turtle.Turtle()

def square_flower(s):
    for i in range(s):
        for i in range(4):
            t.fd(100)
            t.lt(90)
        t.rt(360 / s)

square_flower(10)
