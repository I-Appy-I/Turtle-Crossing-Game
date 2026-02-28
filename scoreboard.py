from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}" , align="center" , font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over" , align="center" , font= FONT)