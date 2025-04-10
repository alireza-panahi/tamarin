name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
import random as R
Suits =['clubs','dimends','hearts','spades']
Ranks=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
# کارت ها و اعداد را وارد میکنیم
temp=0
ranks=R.randrange(0,len(Ranks))
uits=R.randrange(0,len(Suits))
deck=[]
for ranks in Ranks:
    for suits in Suits:
        card= ranks+'of'+suits
        deck+=[card]
# تمامی 52 عدد مارت را میسازیم
for i in range (len(deck)):
    r=R.randrange(0,i+1)
    temp=deck[i]
    deck[i]=deck[r]
    deck[r]=temp
# با استفاده از جابه حا کردن کارت ها را بر میزنیم
print(deck)