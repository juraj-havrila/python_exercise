import turtle
from turtle import Turtle
import time

import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
#car_shape = ((-20,10),(-17,10) ,(-17,12),(-10,12),(-10,10),(10,10),(10,12),(17,12),(17,10), (20, 10), (20, -10), (17,-10),(17,-12),(10,-12),(10,-10),(-17,-10),(-17,-12),(-12,-12),(-12,-10),(-10,-10), (-20, -10))
CAR_SHAPE=((10,-20),(10,-17),(12,-17),(12,-10),(10,-10),(10,10),(12,10),(12,17),(10,17),(10,20),(-10,20),(-10,17),(-12,17),(-12,10),(-10,10),(-10,-17),(-12,-17),(-12,-12),(-10,-12),(-10,-10),(-10,-20))
STARTING_POSITION =((250,250),(250,150),(250,50),(250,-50),(250,-150))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#move_distance=STARTING_MOVE_DISTANCE

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance=STARTING_MOVE_DISTANCE
        self.create_car()


    def move(self):
        self.forward(self.move_distance)


    def speed_up(self):
        self.move_distance += MOVE_INCREMENT

    def create_car(self):
        self.setheading(180)
        turtle.register_shape("car", CAR_SHAPE)
        self.shape("car")
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(random.choice(STARTING_POSITION))





