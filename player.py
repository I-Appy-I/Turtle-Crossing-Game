from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor() , new_y)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def has_player_won(self):
        if self.ycor() > FINISH_LINE_Y:
            self.reset_player()
            return True
        return False