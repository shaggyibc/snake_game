from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
points = 0
screen = Screen()
screen.screensize(600, 600, "black")
screen.title("Is that a snake in your pants?")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 50:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # detect collision with walls
    if snake.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor() > 580 or snake.head.ycor() < -580:
        scoreboard.reset()
        snake.reset()


    # detect collision with tail
    #if the head collides with any segment in the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()