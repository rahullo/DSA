from turtle import *
title('Jai Shree Ram')
bgcolor('white')
pensize(5)
pencolor("ORANGE")
Ram_naam = ["जय श्री राम"]*50
angle = 360/50
penup()
sety(-1)
for _ in range(51):
    left(angle)
    forward(260)
    if Ram_naam:
        write(Ram_naam.pop(), align='center', font=('Arial', 12, 'normal'))
    backward(260)
penup()
goto(-40, -20)
pendown()
write("|| जय श्री राम ||", align='center', font=('Arial', 16, 'bold'))
hideturtle()
done()
