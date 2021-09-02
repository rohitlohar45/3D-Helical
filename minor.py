import turtle
from random import randint

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')

t.speed(0)
t.shape("classic")
t.penup()

t.pendown()

x= 1   

while x<400:
      r=randint(0,255)
      g=randint(0,255)
      b=randint(0,255)
      wn.colormode(255)
      t.pencolor(r,g,b) 
      t.fd(50+x)
      t.rt(90.91)
      x=x+1
wn.exitonclick()    
    