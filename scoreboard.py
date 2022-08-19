from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(shape="classic")
        self.scoreTally = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.show_score()

    def score(self):
        self.scoreTally += 1
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Courier", 20, "normal"))

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.scoreTally}", False, align="center", font=("Courier", 20, "normal"))