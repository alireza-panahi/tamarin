name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
class human: #-------------------------------------------------------------------------------------------------------انسان ها
    total=0 
    def __init__(self,firstname,lastname,gender,nt_num,age,height,weight,city):
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.national_number=nt_num
        self.age=age
        self.haight=height
        self.weight=weight
        self.city=city
        human.total+=1
        if self.gender== 'man' or self.gender== 'male':
            self.call='mr'
        if self.gender == 'woman' or self.gender=='female':
            self.call='ms'
    def get_info(self): #-----------------------------------------------------------------تابع دریافت مشخصات انسان ها
        info=f'{'information of '+ self.lastname:_^50}'
        return('{7}\nFullname={8}.{0}-{1}\nNational Number= {2:010d}\nAge= {3} \nHaight= {4} \nWeight= {5}\nCity= {6}'
               .format(self.firstname,self.lastname,self.national_number,self.age,self.haight,self.weight,self.city,info,self.call))
    def population(): #---------------------------------------------------------------------------------جمعیت انسان ها
        return ('the total population of human in the program is {:03d}'.format(human.total))

class professor(human):#-----------------------------------------------------------------------------------------------اساتید
    id={}
    list={}
    code=1404104070000
    def __init__(self, firstname, lastname,gender, nt_num, age, height, weight, city,classcode):
        super().__init__(firstname, lastname,gender, nt_num, age, height, weight, city)
        professor.code+=classcode
        self.classcode=classcode
        self.professor_id=professor.code
        professor.id[self]=self.professor_id
        professor.list[classcode]=self.lastname
    # ----------------------------------------------------------------------------------------------تابع جمعیت اساتید
    def population():
        return ('the total population of professors in the program is {:03d}'.format(len(professor.id)))
    # ----------------------------------------------------------------------------------------------تابع اطلاعات اساتید
    def get_info(self):
        base_info = super().get_info()
        return ('{1}\nprofessor-id= {0:014d}\nclass= {2}\n{3}'
                .format(self.professor_id,base_info,classes[self.classcode],f'{'_':_^50}'))
    # ----------------------------------------------------------------------------------------------تابع حذف دانشجو
class student(human):#---------------------------------------------------------------------------------------------دانشجو ها
    # id=[]
    id={} #-------------------------------------------------------------------------------------شماره دانشجویی هر فرد
    code=2221040709000 #رفرنس شماره دانشجویی
    def __init__(self, firstname, pastname,gender, nt_num, age, height, weight, city,term,moadel):
        super().__init__(firstname, pastname,gender, nt_num, age, height, weight, city) #ارث گیری از انسان ها 
        self.term=term
        self.moadel=moadel
        self.lession=[] #کلاس های دانشجو
        student.code+=1
        self.student_number=student.code
        # student.id.append(self.student_number)
        student.id[self]=self.student_number #----------------------------------------------اضافه کردن شماره دانشجویی
    # --------------------------------------------------------------------------------------تابع دریاقت اطلاعات دانشجو
    def get_info(self):
        base_info = super().get_info()
        return ('{1}\nTerm= {2}\nstudent-number= {0:014d}\nmoadel kol= {3:2.2f}\n{4}'
                .format(self.student_number,base_info,self.term,self.moadel,f'{'_':_^50}',f'{'student': ^50}'))
    # ----------------------------------------------------------------------------------------------تابع جمعیت دانشجو
    def population():
        return ('the total population of students in the program is {:03d}'.format(len(student.id)))
    # ----------------------------------------------------------------------------------------------------تابع اخذ کلاس
    def take_class(self,student_number,lession_code):
        # if student_number in student.id:
        if student_number == student.id[self]:
            if classes[lession_code] in self.lession:
                return print('mr.{0} class is alredy taken'.format(self.lastname))
            else:
                self.lession.append(classes[lession_code])
                return print('mr.{0} you take the {1} class whit professor {2}'.format(self.lastname,classes[lession_code],professor.list[lession_code]))
        else:
            return print('you most be student to take a class')
    
#-------------------------------------------------------------------------------------------------------------------فرمان ها     
#------------------------------------------------------------------------------------------تعریف کلاس ها
classes={101:'math',102:'poetery',103:'logic',104:'programing',105:'advance_programing'}
#---------------------------------------------------------------------------- تعریف چند دانشجو و استاد   
s1=student('alireza','panahi','male',123456789,22,175,72,'tehran',3,18.333)
s2=student('amir','lotfi','male',198762345,22,175,72,'tehran',2,19.1)
s3=student('parsa','khani','male',748365291,22,175,72,'karaj',1,0.0)
s4=student('mohammad','amiri','male',124398765,22,175,72,'kermanshah',4,12.2)
s5=student('amirali','danaie','man',987643521,22,175,72,'tehran',4,13.71)
p1=professor('mohammad','haghani','male',896745312,43,190,112,'tehran',101)
p2=professor('hasti','nikomanesh','female',98765232,52,185,60,'tehran',102)
p3=professor('salar','mostafavi','male',981276345,67,155,65,'rasht',103)
p4=professor('amirmohammad','haghighi','male',434367853,31,170,80,'karaj',104)
p5=professor('mehdi','mahmodi','male',220226783,50,180,90,'tehran',105)
#--------------------------------------------------------------------دریافت جمعیت انسان ها و دانشجو ها
print(human.population())
print(student.population())
print(professor.population())
#----------------------------------------------------------------------------------برداشتن یک کلاس دوبار
student.take_class(s1,2221040709001,103)
student.take_class(s1,2221040709001,103)
student.take_class(s2,2221040709002,102)
# ---------------------------------------------------------------------------------چاپ اطلاعات یک دانشجو
print(s1.get_info())
print(p2.get_info())
