import turtle
t = turtle.Turtle()

t.setpos(0, 0)

def draw_bar(t, h):
    height = h
    """ Get turtle t to draw one bar, of height. """
    t.pd()
    t.begin_fill() # Added this line
    t.left(90)
    t.forward(height)
    if h < 0:
        t.pu()
        t.fd(-15)
        t.write(" "+ str(height))
        t.fd(15)
        t.pd()
    if h > 0:
        t.write(" " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.pu()
    t.end_fill() # Added this line
    t.forward(10)


wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = -48, 117, 200, 240, 160, 260, 220

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
