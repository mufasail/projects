from turtle import *

diameter = 40
pop_diameter = 100

def draw_balloon ():
  color("red")
  dot(diameter)

def inflate_balloon ():
  global diameter
  diameter = diameter + 10
  draw_balloon()

  if diameter >= pop_diameter:
    clear()
    diameter = 40
    write("POP!")
    
draw_balloon()

Screen().onkey(inflate_balloon, "Up")

Screen().listen()

done()


