from turtle import Turtle
import time

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        # self.write(f"Score: {self.score}", align="center")
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Final Score: {self.score}", align="center")
        time.sleep(1.0)
        self.clear()
        self.write("Game Over....", align="center")
        time.sleep(2.0)
        self.clear()
        self.write("Click to Exit", align="center")


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
        
