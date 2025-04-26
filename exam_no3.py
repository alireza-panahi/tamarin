name: str='dr.ardestani---alireza-panahi---test-no.3'
print(f'{name:_^50}')
# -------------------------------------------------------
import random as R
def numberlist():
    x=[]
    for i in range(20):
        a=R.randrange(1,16)
        x.append(a)
    x.sort()
    return x
def sumlist():
    x=numberlist()
    print(x)
    sum=[]
    for i in range(len(x)):
        for o in range(i+1,len(x)):
            for p in range (o+1,len(x)):
                for k in range (p+1,len(x)):
                    s=x[i]+x[o]+x[p]+x[k]
                    if 50 <= s <=52:
                        sum.append(x[i])
                        sum.append(x[o])
                        sum.append(x[p])
                        sum.append(x[k])
                        print(sum)
                        return sum
                        #این حلقه مجموعه های 4 تایی رو چک میکنه
    for i in range(len(x)):
        for o in range(i+1,len(x)):
            for p in range (o+1,len(x)):
                for k in range (p+1,len(x)):
                    for l in range (k+1,len(x)):
                        s=x[i]+x[o]+x[p]+x[k]+x[l]
                    if 50 <= s <=52:
                        sum.append(x[i])
                        sum.append(x[o])
                        sum.append(x[p])
                        sum.append(x[k])
                        sum.append(x[l])
                        print(sum)
                        return sum
                    #اگه مجموعه 4 تایی نبود این حله احتمال محموعه 5 تایی رو چک میکنه
    for i in range(len(x)):
        for o in range(i+1,len(x)):
            for p in range (o+1,len(x)):
                for k in range (p+1,len(x)):
                    for l in range (k+1,len(x)):
                        for t in range (l+1,len(x)):
                            s=x[i]+x[o]+x[p]+x[k]+x[l]+x[t]
                        if 50 <= s <=52:
                            sum.append(x[i])
                            sum.append(x[o])
                            sum.append(x[p])
                            sum.append(x[k])
                            sum.append(x[l])
                            sum.append(x[t])
                            print(sum)
                            return sum
                        #مثل حلقه قبل ولی برای 6 تایی
sumlist()

