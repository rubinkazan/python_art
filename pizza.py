import turtle

turtle.speed("fastest")
turtle.bgcolor("black")
turtle.pencolor('white')
turtle.begin_fill()

def polygon(a, n):
    for i in range(n):
        turtle.forward(a)
        turtle.left(360/n)
	
for j in range(32):
   	polygon(6*j, 3)
   	turtle.left(30)


turtle.hideturtle()
turtle.speed(0)
turtle.done()
