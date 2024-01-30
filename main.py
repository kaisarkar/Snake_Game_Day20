from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments)-1, 0, -1):
        new_x = segments[segment-1].xcor()
        new_y = segments[segment].ycor()
        segments[segment].goto(new_x, new_y)

    segments[0].forward(20)











screen.exitonclick()