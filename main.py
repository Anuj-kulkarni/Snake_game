from turtle import Screen
from snake import Snake
from Food import Food
from score import ScoreBoard 
import time

screen = Screen()
screen.bgcolor("black")
screen.bgpic("ASK.png")
screen.title("Snake Game")
screen.setup(width=600, height=600)

Snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(Snake.up,"Up")
screen.onkey(Snake.down,"Down")
screen.onkey(Snake.left,"Left")
screen.onkey(Snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()

    if Snake.head.distance(food) < 25:
        food.refresh()
        Snake.extend()
        score.increase_score()

    if Snake.head.xcor() > 280 or Snake.head.xcor() < -280 or Snake.head.ycor() > 280 or Snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in Snake.segments[1:]:

        if Snake.head.distance(segment) < 15:
            game_is_on = False
            score.game_over()

screen.exitonclick()