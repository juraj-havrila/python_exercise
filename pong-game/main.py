from turtle import Screen
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True

while game_is_on:

    screen.listen()
    screen.update()
    
screen.exitonclick()
