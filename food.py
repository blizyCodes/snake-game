from turtle import Turtle
import random
from unicodedata import name


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=2.5, stretch_wid=2.5)
        self.color("red")
        self.speed("fastest")
        self.reappear()

    def reappear(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
