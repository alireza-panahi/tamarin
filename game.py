name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import turtle as T
import math as M
import time
def title ():
    T.penup()
    T.goto(-50,-50)
    T.write(name)
    T.pendown()
title()
screen = T.Screen()
# -----------------------------------------------تابع ادمک هدف
T.speed(0) #بالا ترین سرعت ترتل 
# T.tracer(0)
T.penup()
T.goto(400,50)
T.pendown()
T.fd(200)
T.goto(500,50)
T.lt(90)
T.fd(80)
T.rt(90)
T.circle(30)
T.rt(90)
T.fd(10)
T.lt(90)
T.fd(15)
T.rt(90)
T.fd(30)
T.lt(180)
T.fd(30)
T.lt(90)
T.fd(30)
T.lt(90)
T.fd(30)
T.lt(90)
T.penup()
T.goto(-600,-40)
T.pendown()
T.fd(200)
T.goto(-500,-40)
T.lt(90)
T.fd(30)
T.rt(60)
T.fd(20)
T.lt(90)
T.fd(20)
T.lt(90)
T.fd(115)
T.lt(150)
T.fd(35)
T.lt(30)
T.fd(40)
T.rt(70)
T.fd(32)
T.lt(30)
T.penup()
# -----------------------------------------------تابع و محاسبات پرتاب شلیک
def arrow():
    a= T.Turtle()
    a.speed(0)
    a.shape("circle")
    a.penup() 
    x0=-490
    y0=8
    x=x0
    y=y0
    # a.penup()
    a.goto(x0,y0)
    a.speed(1)
    v0=float(input('please input the power(speed)'))
    deg=float(input('please input the degree'))
    deg_rad = M.radians(deg)
    g = 9.81
    t_prime = 0.5
    t=0
    vx = v0 * M.cos(deg_rad)
    vy = v0 * M.sin(deg_rad)
    while 1>0:
        x = x0 + vx * t
        y = y0 + vy * t - 0.5 * g * t**2
        a.goto(x,y)
        t+=t_prime
        if y< y0:
            break
# 
arrow()

T.done()