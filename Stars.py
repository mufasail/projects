from turtle import *
from random import *
speed(0)
bgcolor("black")
hideturtle()
width = window_width()
height = window_height()
def draw_star(xpos, ypos):
    for _ in range(100):
        size = randrange(1, 5)
        penup()
        goto(xpos, ypos)
        pendown()
        dot(size, "white")
        xpos = randrange(round(-width / 2), round(width / 2))
        ypos = randrange(-height / 2, height / 2)
draw_star(0, 0)
done()
