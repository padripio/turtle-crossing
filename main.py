import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)


score=Scoreboard()
#screen.onkey(key="Up", fun=player.move_up)
#screen.onkey(key="Down",fun=player.move_down)


def main():
    screen.tracer(0)
    screen.listen()

    speed=0
    def run_game():
        game_is_on = True
        count = 4
        cars_list = []
        player = Player()
        x=5

        screen.onkey(key="Up", fun=player.move_up)
        screen.onkey(key="Down", fun=player.move_down)
        while game_is_on:
            #detect finish line


            score.write_score()
            score.write_level()
            count+=1



            if count%5==0:
                cars=CarManager()
                cars_list.append(cars)

            for car in cars_list:
                car.car.speed(x)
                car.move_cars(x)
                if car.car.distance(player.t)<15:
                    score.game_over()
                    level_up=0
                    return level_up

            if player.t.ycor() > 310:
                x+=0
                score.update_score()
                # turtle.clearscreen()


                player.goto_start()

            time.sleep(0.1)
            screen.update()

    lvl=1

    while True:
        run_game()
        #turtle.clearscreen()
        #lvl+=1


    turtle.mainloop()

if __name__=="__main__":
    main()