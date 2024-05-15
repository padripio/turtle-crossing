import turtle
import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

list1=[]
for i in range(-300,300):
    if i%20==0:
        list1.append(i)



class CarManager:
    def __init__(self):
        self.MOVE_INCREMENT=5
        self.car=turtle.Turtle()
        self.car.penup()
        self.car.shape("square")
        self.car.shapesize(stretch_wid=1,stretch_len=2)
        color=random.choice(COLORS)
        self.car.color(color)
        y = random.choice(list1)
        self.car.goto(320, y)
        self.car.setheading(180)
        x=random.randint(1,5)
        self.car.fd(STARTING_MOVE_DISTANCE)

    #TODO start r to l motion

    def move_cars(self,speed):
        self.car.speed(speed)
        self.car.fd(speed)
