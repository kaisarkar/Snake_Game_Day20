from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self, start_position):
        self.starting_position = start_position
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in self.starting_position:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)
