from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

in_game = True
while in_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #This is to detect the collision between the snake and the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #This detects collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #This detects collision with the tail
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
           scoreboard.reset()
           snake.reset()

# tim_2 = Turtle("square")
# tim_2.color("white")
# tim_2.goto(-20, 0)
#
# tim_3 = Turtle("square")
# tim_3.color("white")
# tim_3.goto(-40, 0)





















screen.exitonclick()