from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, start_position):
        self.starting_position = start_position
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    """ Create the snake - starting with 3 segments"""
    def create_snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    """ Add a segment to the snake """
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    """ Extend the snake by adding a segment to the end of the snake """
    def extend(self):
        self.add_segment(self.segments[-1].position())

    """ Move the snake"""
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
