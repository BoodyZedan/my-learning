from random import *
import turtle as t

timmy_tim = t.Turtle()
t.colormode(255)

timmy_tim.speed(100)
timmy_tim.width(20)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color
timmy_tim.color(random_color())
for i in range(360):
    timmy_tim.rt(1)
    for i in range(360):
        timmy_tim.fd(1)
        timmy_tim.rt(1)
    timmy_tim.color(random_color())

screen = t.Screen()

screen.exitonclick()
