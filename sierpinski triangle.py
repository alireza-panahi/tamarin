name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import turtle as T #تابع ترتل برای ترسیم
import random as R #تابع رندوم برای انتخاب راس رندوم 
import math as M #تابع رباضی برای محاسبه مکان ها 
def triangle():
    for i in range(3):
        T.forward(400)
        T.left(120)
def title ():
    T.penup()
    T.goto(-50,-50)
    T.write(name)
    T.pendown()
title()
A=(-200,0) #مکان راس اول
B=(200,0) #مکان راس دوم 
C=(0,(M.sqrt(120000))) #مکان راس سوم 
d=5 #اندازه هر نقطه
T.penup()
T.goto(A)
T.pendown()
#مختصات شروع رسم
triangle()
T.penup()
T.goto(A)
T.color('green')
T.dot(d)
T.goto(B)
T.color('blue')
T.dot(d)
T.goto(C)
T.color('red')
T.dot(d)
T.pendown()
#نقطه های هر راس را با رنگ مربوطه مشخص میکنیم
raas=[A,B,C] #لیست رئوس
L=T.pos() #پیدا کردن مکان فعلی نقطه
T.speed(0) #بالا ترین سرعت ترتل 
T.tracer(0) #انیمشن ترتل بسته میشود برای سرعت بیشتر
s=R.choice(raas) #یک راس رندوم انتخاب میشود
for i in range (5000):
    s=R.choice(raas)
    L=T.pos()   
    x=(L[0]+s[0])/2
    y=(L[1]+s[1])/2
    if s==A:
        T.color('green') 
    elif s==B:
        T.color('blue')
    elif s==C:
        T.color('red') 
    T.penup()
    T.goto(x,y)
    T.dot(d)
    T.pendown()
        #در این حلقه به تعداد 5000 بار یک نثطه تصادقی انتخاب میکند و دقیقا وسط ان نقطه و راس انتخابی را پیدا کرده و نقطه جدید رسم کرده و این کار را تکرار میکند تا در نهایب به مثلث سیرپینسکی برسیم
T.done()
