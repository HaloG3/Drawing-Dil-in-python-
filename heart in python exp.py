
import math
from turtle import* #this is a tool that help to show graphics
def hearta(k):
    return 15*math.sin(k)**3  #maths formula to draw shape
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed (0)   #you can change speed acoording to your wish
bgcolor("black")   # here you can change background colour and look smart
for i in range(6000):
    goto(hearta(i)*15,heartb(i)*19)  # this is the measurement of X axis and Yaxis of heart shape
    for j in range(5):
        color("red")  # this is the colour of heart is going to be drawn
    goto(0,0)
done()

