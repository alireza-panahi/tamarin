name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import turtle as T
T.speed(0) #بالا ترین سرعت ترتل 
# T.tracer(0)
def title ():
    T.penup()
    T.goto(-50,-50)
    T.write(name)
    T.pendown()
title()
n=10
p='power'
def g(m,a):
    angel=120
    n=10
    T.lt(a)
    n=10
    for i in range (n):
        T.forward (p)
        T.right (angel/n)

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
T.goto(-490,10)
T.pendown()
T.pendown()
T.speed(2) 

p=int(input('power -- ghodrat zarbe ra vared konid'))
a=int(input('angel -- zavie partab ra vared konid'))
T.penup()
T.goto(-490,10)
T.pendown()
# p=120
# a=20
g(p,a)
T.done()