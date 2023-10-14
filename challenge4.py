from turtle import Screen
from turtle import Turtle
from turtle import colormode
import random

cursor = Turtle()
colormode(255)


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b,)
    return rgb_color


direction = [0, 90, 180, 270]
# to increase the thickness of line
cursor.pensize(10)
# to speed up the turtle
cursor.speed(7)
for n in range(100):
    # to change the pencolor
    cursor.pencolor(generate_random_color())
    cursor.forward(30)
    # to change the direction randomly
    cursor.setheading(random.choice(direction))
screen = Screen()
screen.exitonclick()
