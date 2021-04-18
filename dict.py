import turtle
turtle.bgcolor("black")
turtle.pensize(1.5)
turtle.speed(0)

for i in range(36):
    for paint in["red","orange","yellow","green","blue","purple"]:
        turtle.color(paint)
        turtle.circle(150)
        turtle.left(50)
        turtle.hideturtle()
turtle.done()




