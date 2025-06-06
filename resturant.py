name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
# -------------------------------------------------------------------------------------------
menu={}
class food ():
    def __init__(self,name,time,amunt,price):
        self.name=name
        self.baking_time=time
        self.amunt=amunt
        self.price=price
        menu[self.name]=('price= {}'.format(self.price))
        self.count=int(amunt)
    def new_price(self,price):
        self.price=price
        print('the new price for {} is set'.format(self.name))
        menu[self.name]=('price= {}'.format(self.price))
    def recepie(self,recepie):
       menu[self.name]=('price= {}'.format(self.price),recepie)

    def order(self):
        if self.count >= 1:
            print('{} is on the way in just {} minutes'.format(self.name,self.baking_time))
            self.count -= 1
            baker.baking()
            return self.count
        else:
            print('Sorry {} is out of stock!'.format(self.name))

class persian_food(food):
    stock=[]
    def __init__(self, name, time, amunt, price):
        super().__init__(name, time, amunt, price)
        persian_food.stock.append(self.name)

    
    
class western_food(food):
    stock=[]
    def __init__(self, name, time, amunt, price):
        super().__init__(name, time, amunt, price)
        western_food.stock.append(self.name)
    

class human:
    def __init__(self,name,lastname,age,id,password):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.id=id
        self.password=password
        self.presence=0

    def arrival_time(self):#------------------------------------------------------------تایم رسیدن
        import time
        current_time = time.strftime("%H:%M:%S", time.localtime())
        temp=int(input('{} inter your password: '.format(self.lastname)))
        if temp == self.password :
            print('your arrival time at {} has bin recorded'.format(current_time))
            self.presence+=1
        else:
            return print('yhe password is wrong1')
    
    def dey_off(self):#----------------------------------------------------------------------مرخصی
        self.presence-=1
        print('{} you take a dayoff'.format(self.lastname))
    
    def present_day(self):#---------------------------------------------------------------روز حضور
        print ('you have been {} day in the company'.format(self.presence))
    
    def pay(self):#----------------------------------------------------------------------حقوق
        pass


class manager(human):
    def __init__(self, name, lastname, age, id, password):
        super().__init__(name, lastname, age, id, password)
    def difine_western_food(self,name,time,amunt,price):
        name=western_food(name,time,amunt,price)
    def difine_persian_food(self,name,time,amunt,price):
        name=persian_food(name,time,amunt,price)

    def fired(self,name):
        temp=int(input('{} inter your password: '.format(self.lastname)))
        if temp == self.password :
            chek=(input('are you shure you want to fire {} ? yes or no '.format(name)))
            if chek == 'yes':
                del employee.members[name]
                print('you fire {}'.format(name))
            else :
                print('the opration canceled')
                

class employee (human):
    members={}
    count=0
    def __init__(self, name, lastname, age, id, password,hiring_date):
        super().__init__(name, lastname, age, id, password)
        self.hiring_date=hiring_date
        employee.members[self.lastname]=('employee')
        employee.count+=1

class baker(employee):
    def __init__(self, name, lastname, age, id, password, hiring_date):
        super().__init__(name, lastname, age, id, password, hiring_date)
        employee.members[self.lastname]=('baker')
    def baking():
        print('the order is on the way')
    



    
class delivery(employee):
    pass
    
class fainacial(employee):
    pass
class cleaner(employee):
    pass
class reception(employee):
    pass
class customer():
    def __init__(self, name, lastname):
       
        self.name=name
        self.lastname=lastname

    def take_order(self):
        print(menu)
        order = input('What do you prefer? ').strip()
        if order in western_food.stock:
            food_instance = next((obj for obj in globals().values() if isinstance(obj, western_food) and obj.name == order), None)
            if food_instance:
                food_instance.order()
            else:
                print('No instance of {} found!'.format(order))
        else:
            print('Sorry {} is not available in the menu!'.format(order))

hemati=manager('mohammad','hemati',45,232323230,1)
ali=employee('ali','panahi',22,222222222,1,404)
amir=baker('amir','mohammadi',22,222222222,1,404)
pizza=western_food('pizza',30,3,50)
hemati.difine_western_food('pasta',20,50,70)

m1=customer('nima','ahmadi')
# print(menu)
# pizza.new_price(30)
# pizza.recepie('peperoni,marshrom,bred,paper,sult,tomato')
# print(menu)
# print(employee.members)
# ali.arrival_time()
# ali.dey_off()
# ali.present_day()
# hemati.fired('panahi')
m1.take_order()
m1.take_order()

m1.take_order()

