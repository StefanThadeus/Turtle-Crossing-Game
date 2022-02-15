import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game!")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.go_up, "Up")

scoreboard = Scoreboard()

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # check if player crossed the road
    if player.crossed_finish():
        player.go_to_start()
        scoreboard.update()
        car_manager.level_up()

    # check if player collided with car
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
