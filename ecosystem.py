name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
# -----------------------------------------
def ecosystem(deer,wolf):
    time=20 # 12 سال
    #نرخ های تعیین شده در اینترنت نبود و دستی تعیین شد
    alpha = 2  # نرخ رشد آهو
    beta = 0.2  # نرخ شکار آهو توسط گرگ
    delta = 0.1  # نرخ افزایش گرگ
    gamma = 1  # نرخ مرگ گرگ
    min = 5  # حداقل جمعیت برای جلوگیری از انقراض

    # تنظیمات زمان
    dt = 1  # گام زمانی
    t=0
    # روش اویلر و شبیه‌سازی
    while t<time:
    # for i in range(n):
        # معادله لوتکا ولترا
        dx = (alpha * deer - beta * deer * wolf) * dt
        dy = (delta * deer * wolf - gamma * wolf) * dt
        
        deer += dx
        wolf += dy
        t+=dt

        if deer < min:
            deer = min
        if wolf < min:
            wolf = min
            
        print ('time{:.1f} | population of {:.1f} | population{:.1f}'.format(t, deer,wolf))
ecosystem(50,10)