name: str='dr.ardestani---alireza-panahi---test-no.1'
print(f'{name:_^50}')
import turtle as T
def title ():
    T.penup()
    T.goto(-450,-50)
    T.write(name)
    T.pendown()
# ---------------------------------------------------------
A=T.Turtle()
angel=360
# x=[]
T.speed(0)
#تابع رسم شکل ان وجهی
def shape(n):
    A.color('red')
    for i in range (n):
        A.fd(100)
        A.lt(angel/n)
        # x.append(A.pos())
#شکل ان وجهی قرینه اولی
def shape2(n):
    for i in range(n):
        A.fd(100)
        A.rt(angel/n)
#تابع قرار دادن دو شکل اول در کنار هم        
def montazam(n):
    if n <=2:
        print('numer cant be <= 2')
    else:
        title()
        shape(n)
        A.color('black')
        for i in range (n):  
            shape2(n)
            A.fd(100)
            A.lt(angel/n)
    T.done()  

montazam(6)