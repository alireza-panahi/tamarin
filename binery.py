name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
#دریافت عدد مورد نیاز برای تبدیل
x=int(input('x'))
b=''
code=b
#دراین بخش عدد را داخل یک چرخه قرار میدهیم که تا وقتی صفر نشده تقسیم بر دو کند و باقی مانده را در یک رشته ذخیره کند
while x>0:
    b=x%2
    x=x//2
    code=str(b)+code
print(code)
