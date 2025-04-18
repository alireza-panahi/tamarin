name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import turtle as T
import random as R
tree=T.Turtle()
screen=T.Screen()
screen.setup(width=600,height=600)
scale = 50
screen.setworldcoordinates(-6,-1,6,11)
T.write(name)
tree.color('green')
y=0
x=0
for i in range (5000):
    r=R.random()
    # احتمالات گفته شده سر کلاس
    # if r<0.02 :
    #     x_new=0.5
    #     y_new=0.27 * y
    # elif r<0.17:
    #     x_new=-(0.14*x)+(0.26*y)+0.57
    #     y_new=0.25*x+0.22*y-0.04
    # elif r<0.30:
    #     x_new=0.17*x-0.21*y+0.41
    #     y_new=0.22*x+0.18*y+0.9
    # else:
    #     x_new=0.78*x+0.03*y+0.11
    #     y_new=-0.03*x+0.74*y+0.27
    # احتمالات گفته پیدا شده در اینترنت
    if r < 0.01:
        x_new=0
        y_new =0.16*y
    elif r < 0.86:
        x_new = 0.85*x + 0.04*y
        y_new = -0.04*x + 0.85*y + 1.6
    elif r < 0.93:
        x_new = 0.2*x - 0.26*y
        y_new = 0.23*x + 0.22*y + 1.6
    else:
        x_new = -0.15*x + 0.28*y
        y_new = 0.26*x + 0.24*y + 0.44
    x=x_new
    y=y_new
    T.tracer(0)
    tree.speed(0)
    tree.penup()
    tree.goto(x,y)
    tree.dot(5)
    print(r)

T.done()