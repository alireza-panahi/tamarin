#ALIREZA PANAHI
year=int(input('input the year')) #سال را از مخاتب دریافت کرده و به فرمت اینت تبدیل میکنیم
if (year % 4==0 and year % 100 != 100)or(year % 400 == 0): #با دستور ایف و فرمول سال کبیسه داده را مقایسه میکنیم
    print(f'the year {year} is a leap year') #در صورت درست بودن فرمول ها پیام این سال کبیسه است چاپ میشود
else:
    print(f'the year {year} is not a leap year') #در غیر این صورت پیام این سال کبیه نیست چاپ میشود
