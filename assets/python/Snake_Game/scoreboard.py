from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,220)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'bold'))


    def game_over(self):
        self.clear()
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(0,0)
        self.write(f"GAME OVER\nFinal Score: {self.score}", align="center", font=("Arial",24, 'bold'))
    def increase_score(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()
