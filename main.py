from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Score


screen = Screen()
screen.title("3310 nostalgia")
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkeypress(snake.turn_up, "w")
screen.onkeypress(snake.turn_up, "W")
screen.onkeypress(snake.turn_down, "s")
screen.onkeypress(snake.turn_down, "S")
screen.onkeypress(snake.turn_left, "a")
screen.onkeypress(snake.turn_left, "A")
screen.onkeypress(snake.turn_right, "d")
screen.onkeypress(snake.turn_right, "D")


game_on = True


while game_on:
    if 0 < len(snake.snakes) < 8:
        speed = 0.2
    elif 8 < len(snake.snakes) < 20:
        speed = 0.18
    elif 20 < len(snake.snakes) < 30:
        speed = 0.16
    elif 30 < len(snake.snakes) < 40:
        speed = 0.12
    elif len(snake.snakes) > 50:
        speed = 0.1

    screen.update()
    time.sleep(speed)
    snake.move_snakes()

    # detecting when food is eaten
    if snake.head.distance(food) < 15:
        food.reappear()
        score.increment()
        snake.extend_tail()

    # detecting snake hitting the wall
    if (
        snake.head.xcor() > 580
        or snake.head.xcor() < -580
        or snake.head.ycor() > 580
        or snake.head.ycor() < -580
    ):
        game_on = False
        score.game_over()

    # detecting snake hitting itself
    for snake_part in snake.snakes[1:]:
        if snake.head.distance(snake_part) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
