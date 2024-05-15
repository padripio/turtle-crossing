import turtle,time
from turtle import Turtle
STARTING_POSITION = (0, -300)

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.t=turtle.Turtle()
        self.t.shape("turtle")
        self.t.setheading(90)
        self.t.shapesize(1)
        self.t.penup()
        self.goto_start()
        self.can_move=True

    def reset_movement(self):
        self.can_move=True

    def move_up(self):
        if self.can_move:
            self.t.speed("fastest")
            self.t.fd(10)
            self.can_move=False
            turtle.ontimer(fun=self.reset_movement,t=10)
        #time.sleep(0.2)
    def move_down(self):
        stop=1
        if self.can_move:
            self.t.fd(0)
            self.can_move = False
            turtle.ontimer(fun=self.reset_movement, t=300)

    def goto_start(self):
        self.t.goto(STARTING_POSITION)



