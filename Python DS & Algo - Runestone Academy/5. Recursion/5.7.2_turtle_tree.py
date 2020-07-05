import turtle
import random


def tree(branchLen, t, r, g, b):
    if branchLen > 5:
        t.color(r, g, b)
        t.pensize(branchLen//10)
        t.forward(branchLen)
        random_angle = random.randint(15, 45)
        branch_subtract_length = random.randint(10, 20)
        t.right(random_angle)
        tree(branchLen - branch_subtract_length, t, r + 4, g + 15, b)
        t.left(random_angle * 2)
        tree(branchLen - branch_subtract_length, t, r + 4, g + 15, b)
        t.right(random_angle)
        t.backward(branchLen)


t = turtle.Turtle()
myWin = turtle.Screen()
myWin.colormode(255)
turtle.speed(0)
t.left(90)
t.up()
t.backward(100)
t.down()
t.color(150, 97, 17)
r = 50
g = 97
b = 18
tree(100, t, r, g, b)
myWin.exitonclick()
