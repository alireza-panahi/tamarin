name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import random as R
x=[0,4,3,0,1,7,9,3,2,4]
print('code meli = {0}'.format(x))
# بردار کد ملی را تغریف کردیمم
mat1=[]
mat2=[]
# ماتریس های شماره 1 و 2 هم تعریف میکنیم
# در تابع زیر به تعداد رقم های کد ملی بردار مختلف میسازیم
def mat (m,x):
    for i in range(10):
        random=x.copy()
        for i in range(len(x)):
            r=R.randrange(len(x))
            random[i],random[r]=random[r],random[i]
        m.append(random)
    return(m)
# با استفاده از تابع ساخته شده ماترس های 1 و 2 را میسازیم و پرینت میکنیم
matrice1=mat(mat1,x)
print('matrice1 = {0}'.format(matrice1))
matrice2=mat(mat2,x)
print('matrice2 = {0}'.format(matrice2))
# یک تابع برای جمع ماتریس ها میسازیم 
def sum (x,y):
    res=[]
    for i in range(len(x)):
        new=[]
        for j in range(len(x[0])):
            new.append(x[i][j]+y[i][j])
        res.append(new)
    return res
# ماتریس های دریاقت شده را با هم جمع میکنیم و پرینت میکنیم 
s=sum(matrice1,matrice2)
print('matrice 1 + matrice 2 = {0}'.format(s))
# یک تابع برای ضرب ماترس ها میسازیم
def multiply(x,y):
    res=[[0]*(len(x)) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(10):
            temp=0
            for k in range(10):
                temp+=x[i][k]*y[k][j]
            res[i][j]=temp
    return res
# ماتریس های دریاقت شده را در هم ضرب  میکنیم و پرینت میکنیم 
m=multiply(matrice1,matrice2)
print('matrice 1 * matrice 2 = {0}'.format(m))
