from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):

        for position in STARTING_POSITIONS:
            self.add_tail(position)

    def move_snakes(self):

        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x_cord = self.snakes[snake_num - 1].xcor()
            new_y_cord = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x_cord, new_y_cord)

        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_tail(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend_tail(self):
        self.add_tail(self.snakes[-1].position())
