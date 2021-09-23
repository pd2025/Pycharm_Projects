import turtle

t = turtle.Turtle()

def square_spiral_1():
    p = 0
    for i in range (50):
        t.fd(p)
        t.lt(90)
        p = p + 10

#square_spiral_1()

def square_spiral_2():
    p = 0
    for i in range (100):
        t.fd(p)
        t.lt(85)
        p = p + 2

square_spiral_2()