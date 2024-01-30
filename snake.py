starting_position = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in starting_position:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.segments[0].forward(20)
