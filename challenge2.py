from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
for n in range(25):
    if n%2==1:
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pencolor("black")
    else:
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pencolor("white")

screen = Screen()
screen.exitonclick()
