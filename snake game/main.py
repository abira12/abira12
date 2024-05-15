from turtle import Screen,Turtle
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Welcome to snake game")
segments=[]
turtle_1=Turtle("circle")
turtle_1.color("white")
turtle_1.penup()
segments.append(turtle_1)
turtle_2=Turtle("square")
turtle_2.color("white")
turtle_2.penup()
turtle_2.goto(-20,0)
segments.append(turtle_2)
turtle_3=Turtle("triangle")
turtle_3.color("white")
turtle_3.penup()
turtle_3.goto(+20,0)
segments.append(turtle_3)
game=True
while game:
    for seg in segments:
        seg.forward(10)













screen.exitonclick()