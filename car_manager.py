from turtle import Turtle
import random

CAR_IMAGES = [
    "assets/cars/red_car.gif",
    "assets/cars/green_car.gif",
    "assets/cars/yellow_car.gif",
    "assets/cars/brown_car.gif",
    "assets/cars/black_car.gif",
    "assets/cars/orange_car.gif",
    "assets/cars/purple_car.gif"
]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
LANES = [-200, -150, -100, -50, 0, 50, 100, 150, 200]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        if random.randint(1, 6) == 1:
            random_y = random.choice(LANES)

            is_lane_clear = True
            for car in self.all_cars:
                # Spawn point is 320. If any car is in the same lane and
                # has not reached x=100 yet, it's too close for a new spawn.
                # This creates a 220-pixel safety buffer.
                if car.ycor() == random_y and car.xcor() > 100:
                    is_lane_clear = False
                    break

            if is_lane_clear:
                random_car_path = random.choice(CAR_IMAGES)
                new_car = Turtle(random_car_path)
                new_car.penup()
                new_car.setheading(180)
                new_car.goto(320, random_y)
                self.all_cars.append(new_car)

    def move_cars(self):
        """Moves cars and removes those that leave the screen."""
        for car in self.all_cars:
            car.forward(self.car_speed)

        # Memory cleanup: remove cars once they are fully off-screen
        self.all_cars = [car for car in self.all_cars if car.xcor() > -350]

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT