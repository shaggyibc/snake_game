from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=20, stretch_wid=1)
        self.speed("fastest")
        self.goto(0, 250)
        self.score = 0
        with open(file="/Users/insse/OneDrive/desktop/data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}  High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            with open("/Users/insse/OneDrive/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def get_saved_high_score(self):
    #     with open("\Users\insse\OneDrive\desktop\data.txt") as file:
    #         high_score = file.read
    #         return high_score

