name: str='dr.ardestani---alireza-panahi---test-no.2'
print(f'{name:_^50}')
# -------------------------------------------------------
def a_prime (num):#تابع برای چک کردن عدد اول بودن
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
#تابع دادن زد عدد اول بعد از غدد داده شده
def prime_num(n,z):
    x=a_prime(n)
    a=[]
    i=1
    if x == True:
        print('{} it is a prime number'.format(n))
    elif x == False:
        print ('{} is not a prime number'.format(n))
    while (len(a)) < z :
        m=a_prime(n+i)
        if m == True:
            a.append(n+i)
        i+=1
    print ('{0}end prime number after {1} = {2} '.format (z,n,a[-1]) )
    return (a[-1])
prime_num(100,7)
