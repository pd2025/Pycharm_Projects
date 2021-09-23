import turtle
t = turtle.Turtle()

def polygons(n):
    for i in range (n):
        t.fd(100)
        t.lt(360/n)

polygons(8)