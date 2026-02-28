from turtle import Turtle

ROAD_START_Y = -225
ROAD_END_Y = 225
SAFE_ZONE_HEIGHT = 75


class RoadEnv:
    def __init__(self):
        self.painter = Turtle()
        self.painter.hideturtle()
        self.painter.speed(0)
        self.draw_world()

    def draw_world(self):
        self.painter.penup()

        # 1. Draw Gray Road
        self.painter.goto(-300, ROAD_START_Y)
        self.painter.color("dimgray")
        self.painter.begin_fill()
        for _ in range(2):
            self.painter.forward(600)
            self.painter.left(90)
            self.painter.forward(450)  # Distance from -225 to 225
            self.painter.left(90)
        self.painter.end_fill()

        # 2. Draw Green Grass (safe parts
        self.draw_safe_zone(-300, -300)  # Bottom
        self.draw_safe_zone(-300, ROAD_END_Y)  # Top

        # 3. Draw Lane Lines
        self.draw_lane_dividers()

    def draw_safe_zone(self, x, y):
        self.painter.goto(x, y)
        self.painter.color("forest green")
        self.painter.begin_fill()
        for _ in range(2):
            self.painter.forward(600)
            self.painter.left(90)
            self.painter.forward(SAFE_ZONE_HEIGHT)
            self.painter.left(90)
        self.painter.end_fill()

    def draw_lane_dividers(self):
        self.painter.color("white")
        self.painter.pensize(2)
        # Draws a line between each of your car lanes
        for y in range(-175, 225, 50):
            self.painter.goto(-300, y)
            self.painter.setheading(0)
            for _ in range(15):
                self.painter.pendown()
                self.painter.forward(20)
                self.painter.penup()
                self.painter.forward(20)