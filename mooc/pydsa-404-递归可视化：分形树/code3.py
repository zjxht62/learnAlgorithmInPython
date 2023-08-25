import turtle

t = turtle.Turtle()
t.pensize(3)
t.pencolor('red')

for i in range(5):
    t.forward(100)
    t.right(144)

t.hideturtle()

turtle.done()