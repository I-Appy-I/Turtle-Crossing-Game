import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from roads import RoadEnv

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#  initialize the background first so it's behind everything
env = RoadEnv()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

#  register shapes
for image in ["assets/cars/red_car.gif", "assets/cars/green_car.gif", "assets/cars/yellow_car.gif",
              "assets/cars/brown_car.gif", "assets/cars/black_car.gif", "assets/cars/orange_car.gif",
              "assets/cars/purple_car.gif"]:
    screen.register_shape(image)

screen.listen()
screen.onkeypress(player.go_forward, "Up")

game_is_on = True
speed = 0.01
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # accurate car collision detection
    for car in cars.all_cars:
        car_y = car.ycor()
        if (player.ycor() < car_y + 20) and (player.ycor() > car_y - 22):
            if player.distance(car) < 30:
                game_is_on = False
                car.goto(car.xcor(), car.ycor())
                screen.update()
                scoreboard.game_over()

    # winning condition nd increasing speed each time
    if player.has_player_won():
        scoreboard.increase_score()
        cars.increase_speed()

screen.exitonclick()