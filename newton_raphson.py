name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
#کتابخانه رندوم را برای گرفتن عدد رندوم وارد میکنیم 
import random
#تابع مورد نظر را وارد میکنیم 
def f(x):
    return (2*x**3)+(2*x**2)+(x)+(6)
# مشتق تابع مورد نظر را وارد میکنیم 
def f_prime(x):
    return (6*x**2)+(4*x)+(1)
#مقدار رندوم را وارد کرده تا روش نیوتن رافسون را شروع کنیم
x=random.randrange(-10,10)
#مرحله را از صفر تا بیست انجام میدهیم
s=0
ms=20
#روش نیوتن رافسون
while s<ms:
    fx=f(x)
    fpx=f_prime(x)

    x_new=x-(fx/fpx)
    print('step {0} x={1} '.format(s+1,x_new))
    if abs(x-x_new)<0.0001:
        print('root={0}'.format(x_new))
        break
    x=x_new
    s=s+1


