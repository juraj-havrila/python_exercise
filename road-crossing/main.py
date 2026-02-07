import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
sleep_time=0.1
traffic=[]
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light gray")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_down,"Down")

game_is_on = True
increase_speed=False
cycle=0
while game_is_on:
    time.sleep(sleep_time)
    cycle+=1
    screen.update()
    if player.ycor() > 290:
        player.reset_position()
        increase_speed=True
        sleep_time *= 0.9
        scoreboard.add_point()

    if cycle > 10:
        cycle =0
        traffic.append(CarManager())
    for car in traffic:
        if increase_speed:
            car.speed_up()
        car.move()
        if car.distance(player) < 20:
            game_is_on = False
            player.dead()
            scoreboard.game_over()

        if (car.ycor() < -300):
            traffic.remove(car)
    increase_speed = False

screen.exitonclick()
