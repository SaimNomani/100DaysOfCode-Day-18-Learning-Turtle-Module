from turtle import Turtle, Screen
import random

cursor = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for n in range(no_of_sides):
        cursor.forward(75)
        cursor.right(angle)


for n in range(3, 11):
    cursor.color(random.choice(colours))
    draw_shape(n)

screen = Screen()
screen.exitonclick()
