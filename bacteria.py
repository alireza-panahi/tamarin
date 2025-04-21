name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
# ----------------------------------------------------------------------------
import random as R
def bacteria (n): #تابع باکتری را میسازیم
    bacteria=1 # متغیر باکتری را  تعریف کردیم
    t=0 #زمان اولیه 
    dead=0 # تعداد باکتری های مرده
    while (bacteria < n): #یک حلقه برای تا وقتی که باکتری ها به تعداد دلخواه برسد ادامه داشته باشد 
        bacteria= bacteria + bacteria #در هر تکرار تعداد باکتری ها دو برار میشود 
        t+=1 #زمان اضافه میشود
        for i in range (bacteria): #حلقه مرگ باکتری ها 
            r=R.random() #یه عدد رندوم بین صفر و یک میسازد
            if r<0.25: #در احتمال 25 درصد یک باکتری را حذف میکند
                bacteria-=1
                dead+=1
    print('in just a {0} seconds the number of bacteria comes to the {1} and in this time {2} bactria died'.format(t,bacteria,dead))

#تابع را برای تعداد یک میلیون باکتری فراخانی میکنیم
bacteria (1000000)