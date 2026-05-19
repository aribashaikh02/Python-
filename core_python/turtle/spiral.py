import turtle

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

sally = turtle.Turtle()
sally.speed(0)
sally.width(2)

for i in range(200):
    sally.pencolor(colors[i % 6])
    sally.forward(i * 3)
    sally.right(67)

turtle.done()