from random import *
import turtle as t

timmy_tim = t.Turtle()
t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

for i in range(500):
    timmy_tim.fd(10)
    timmy_tim.color(random_color())
    rt_lt = randint(1, 2)
    if rt_lt == 1:
        timmy_tim.rt(90)
        timmy_tim.fd(20)
    if rt_lt == 2:
        timmy_tim.lt(90)
        timmy_tim.fd(20)
screen = t.Screen()

screen.exitonclick()
