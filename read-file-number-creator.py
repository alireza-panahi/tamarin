import random as R
file=open('numbers.txt','w') #با این دستور فایل برای ذخیره اعداد ساخنه میشود
for i in range (100):
    number=R.randint(1,100)
    file.write(str(number)+('\n'))
file.close
