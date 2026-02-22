from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import pygame

pygame.init()
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.1)

eat_sound = pygame.mixer.Sound('audio/jump.mp3')

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True

if game_is_on:
    bg_music.play(loops = -1)

    

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#collision with food
    if snake.head.distance(food) < 15:
        eat_sound.play()
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()


#detect colliosn with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()