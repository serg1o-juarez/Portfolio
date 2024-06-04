from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title('🐍 SNAKE 🐍')
screen.tracer(0)
snake = Snake()
food = Food()
scorebaord = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scorebaord.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        game_on = False
        scorebaord.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scorebaord.game_over()




















screen.exitonclick()
