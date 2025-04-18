name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import turtle as T
import random as R
coral=T.Turtle()
screen=T.Screen()
screen.setup(width=900,height=600)
scale = 50
screen.setworldcoordinates(-5,-1,10,11)
T.write(name)
coral.color('coral')
y=0
x=0
for i in range (15000):
    r=R.random()
    if r < 0.4:
        x_new = 0.31*x - 0.53*y + 0.89
        y_new =-0.46*x - 0.29*y + 1.04
    elif r < 0.55:
        x_new = 0.31*x - 0.08*y + .89
        y_new = 0.15*x - 0.45*y + 0.34
    else:
        x_new = 0.55*y + 0.01
        y_new = 0.69*x - 0.20*y + 0.38
    x=x_new
    y=y_new
    T.tracer(0)
    coral.speed(0)
    coral.penup()
    coral.goto(x*5,y*5)
    coral.dot(2)
    # print(r)

T.done()