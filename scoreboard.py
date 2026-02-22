from turtle import Turtle


ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def display_final_score(self):
        self.goto(0, -50)
        self.write(f"Final Score is: {self.score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()