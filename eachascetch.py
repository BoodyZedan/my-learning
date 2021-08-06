from turtle import *
screen = Screen()


def down():
    bk(20)


def up():
    fd(20)


def right():
    rt(10)


def left():
    lt(10)


def penup2():
    penup()


def pendown2():
    pendown()


def clear2():
    reset()


screen.listen()
screen.onkey(clear2, "c")
screen.onkey(pendown2, "d")
screen.onkey(penup2, "u")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.exitonclick()
