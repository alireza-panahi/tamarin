name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
#شروع تمرین (برنامه ایی بنویسید که یک عدد گرفته و دو را به توان اعداد قبل ان برساند) 
#این خط عدد را از کاربر گرفته
x=int(input( 'please inter numper'))
i=0
power=1
#این خط تا زمانی که کارکتر ای به عدد وارد شده برسد دو را به توان ای مرساند و پرینت میکند
while i<=x:
    print('2^'+str(i)+'---->'+str(power))
    i=i+1
    power*=2   
#این خط داخل وی اس کد کاربردی ندارد ولی برای اجرای برنامه در محیط خود پایتون نیاز است تا برنامه بسته نشود
input('perss enter to close the program')