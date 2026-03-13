import turtle
WIDTH = 500
HEIGHT = 500
DELAY = 10

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle Animation")
screen.bgcolor("cyan")

my_turtle = turtle.Turtle()
my_turtle.color("red")
my_turtle.shape("turtle")
screen.tracer(0)

move_turtle()
turtle.done()