name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import turtle as T
import math as M
import random as R
def title ():
    T.penup()
    T.goto(-350,-50)
    T.write(name)
    T.pendown()
title()
# T.tracer(0)
t=T.Turtle()
color=['red','purple','green','yellow','orange','blue','black','cyan']
# t.color('red')
t.speed(0)
x=[]
y=[]
def body (n=50,z=8):
    for i in range(z):
        t.fd(n)
        t.rt(45)
        t.fd(n)
        t.lt(90)
        t.fd(n)
        t.rt(45)
        t.fd(n)
        t.lt(360/z)
    x_new=n+(M.sqrt(n**2+n**2))+n+2*(M.sqrt(((n+(M.sqrt(n**2+n**2))+n)**2)/2))
    y_new=n+(M.sqrt(n**2+n**2))+n+2*(M.sqrt(((n+(M.sqrt(n**2+n**2))+n)**2)/2))
    x.append(x_new)
    y.append(y_new)
#داخل
def inside (n,z):
    for i in range(4):
        # t.color(color[R.randrange(0,(len(color)))])
        body(n,z)
        for i in range(2):
                t.fd(n)
                t.rt(45)
                t.fd(n)
                t.lt(90)
                t.fd(n)
                t.rt(45)
                t.fd(n)
                t.lt(360/8)
#تابع ساخت 4 عدد کنار هم
def slim(n=50,m=3):
    t.penup()
    # body(n,z)
    t.pendown()
    inside(n,m)
    spot=[(0,0),(x[0],0),(0,-y[0]),(x[0],-y[0])]
    for i in range(3):
        t.penup()
        t.goto(spot[i+1])
        t.pendown()
        # body(50,8)
        inside(n,m)
# اکنون با فراخوانی تابع با اعداد مختلف طرح های متفاوت داریم برای مثال با مقیاس 30 و 4 شکل هندسی 
slim(30,4)
#نمونه های کامنت شده زیر اشکال متفاوتی را ارئه میدهند
# slim(15,30)
# slim(20,5)
# slim(40,3)
# slim(25,2)
T.done()