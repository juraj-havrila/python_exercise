import time
from  turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        #game_is_on = False
        #score.game_over()
        score.reset()
        snake.reset()

    for segment in snake.segments[1:-1]:
        #if segment == snake.head:
        #   pass
        if snake.head.distance(segment) < 15:
            #game_is_on = False
            #score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()
