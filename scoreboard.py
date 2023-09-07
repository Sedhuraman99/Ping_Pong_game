from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("courier", 80, "normal"))

    def l_wins(self):
        self.l_score += 1
        self.update_score()

    def r_wins(self):
        self.r_score += 1
        self.update_score()
