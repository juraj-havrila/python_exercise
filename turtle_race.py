from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors=["blue", "green", "yellow", "orange", "red"]
turtles={}
position_y=100
for color in colors:
    turtles[color]=Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(x=-230, y=position_y)
    position_y=position_y-50
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtles[turtle].forward(random_distance)
        if turtles[turtle].xcor() > 230:
            is_race_on = False
            if user_bet == turtle:
                print ("You win!")
            else:
                print (f"You lose! The {turtle} turtle won the race.")
screen.exitonclick()
