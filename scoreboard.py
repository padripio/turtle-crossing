import turtle

FONT = ("Courier", 20, "normal")


class Scoreboard:
    def __init__(self):
        self.score=0
        self.write=turtle.Turtle()
        self.write.hideturtle()
        self.write.penup()

    def write_score(self):
        self.write.clear()
        self.write.goto(-300, 300)
        self.write.write(arg="Score", align="left", font=FONT)
        self.write.goto(-200, 300)
        self.write.write(arg=self.score, align="left", font=FONT)

    def write_level(self):
        #self.write.clear()
        self.write.goto(200, 300)
        self.write.write(arg="Level", align="left", font=FONT)
        self.write.goto(300, 300)
        self.write.write(arg=self.score, align="left", font=FONT)

    def game_over(self):

        self.write.goto(-50, 0)
        self.write.write(arg="Game Over", align="left", font=FONT)



    def update_score(self):
        self.score+=1

