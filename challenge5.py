from turtle import Screen
from turtle import Turtle
import random
import turtle as t

cursor = Turtle()
t.colormode(255)
cursor.speed("fastest")


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b,)
    return rgb_color


for n in range(72):
    cursor.color(generate_random_color())
    cursor.circle(100)
    cursor.right(5)

screen = Screen()
screen.exitonclick()
