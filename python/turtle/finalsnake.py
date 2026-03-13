#Final Snake code

import turtle
import random
import time

# ---------------- SCREEN SETUP ---------------- #
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off automatic screen updates

# ---------------- SNAKE SETUP ---------------- #
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Snake body list
segments = []

#FOOD SETUP#
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# ---------------- SCORE ---------------- #
score = 0

# ---------------- FUNCTIONS ---------------- #
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    x = snake.xcor()
    y = snake.ycor()

    if snake.direction == "up":
        snake.sety(y + 20)
    if snake.direction == "down":
        snake.sety(y - 20)
    if snake.direction == "left":
        snake.setx(x - 20)
    if snake.direction == "right":
        snake.setx(x + 20)

# ---------------- KEYBOARD BINDING ---------------- #
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# ---------------- MAIN GAME LOOP ---------------- #
while True:
    screen.update()
    time.sleep(0.1)

    # Move the snake
    move()

    # Check wall collision
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        print("Game Over! Score:", score)
        break

    # Check food collision
    if snake.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        score += 1

    # Move body segments
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(snake.xcor(), snake.ycor())

turtle.done()