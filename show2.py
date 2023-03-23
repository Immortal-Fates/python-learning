import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angel in [0,60,-120,60]:
            turtle.left(angel)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level=5
    koch(400,5)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()
