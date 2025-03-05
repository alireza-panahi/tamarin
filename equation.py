#شاید نیاز باشد از کد دو بار ران بگیرید و دفعه اول ارور دهد
name: str='dr.ardestani----alireza-panahi'
print(f'{name:_^50}')
#شروع تمرین (برنامهایی بنویسید که معادله درجه دوم را حل کند )
#-----------------------------بخش پرفتن اعداد معادله
print('a(x**2)+b(x)+c')
print('please input number like ebove example')
a=int(input('inter a'))
b=int(input('inter b'))
c=int(input('inter c'))
#--------------------------------بخش حل معادله
import math 
#در این بخش یک تایع مسازیم که ابتدا دلتا رو محاسبه کرده و سپس متناسب با مقدار دلتا اعلام کند که معادله موهومی است یا حقیقی
def solve():
    delta=b**2-4*a*c
#در این بخش اگر مقدار دلتا بزرگتر مساوی 0 باشد اعلام میکند که حقیقیه و با فرمول مقدار ریشه ها را بدست میاورد    
    if delta>=0:
        print('it`s Real number')
        x1=(-b+(math.sqrt(delta)))/(2*a)
        x2=(-b-(math.sqrt(delta)))/(2*a)
#در این بخش اگر مقدار ریشه ها برابر بود هر دو را در یک سطر نمایش میدهد        
        if x1==x2:
            print('x1 & x2= {0}' .format(x1))
#در این بخش ریشه های متفاوت را تفکیک کرده و نمایش میدهد        
        else:
            print('x1= {0}' .format(x1))
            print('x2= {0}' .format(x2))
#در این بخش اگر دلتا کوچک تر از صفر باشد اعلام میکند که موهومیه و فرمول محاسبه معادله موهومی را اجرا میکند     
    elif delta<0:
        print('it`s Imaginary number')
        delta=-delta
        real=(-b/(2*a))
        imag=((math.sqrt(delta))) / (2*a)
# در این بخش اگر عدد موهومی برابر 1 باشد ان را نمینویسد و فقط علامت را نشان میدهد
        if imag==1:
            print('x1= {0} +i' .format(real))
            print('x2= {0} -i' .format(real))
#ریشه های معادله را نشان میدهد        
        else:
            print('x1= {0} +{1}i' .format(real,imag))
            print('x2= {0} -{1}i' .format(real,imag))
solve()
#این خط داخل وی اس کد کاربردی ندارد ولی برای اجرای برنامه در محیط خود پایتون نیاز است تا برنامه بسته نشود
input('perss enter to close the program')