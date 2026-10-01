"""
number1=int(input("Enter 1st id: "))
number2=int(input("Enter 2nd  id: "))
operator=input("Enter Operators")
if operator=="+":
    print(number1+number2)
elif operator=="-":
    print(number1-number2)
elif operator =="*":
    print(number1*number2)
elif operator =="/":
    print(number1/number2)
elif operator =="//":
    print(number1//number2)
elif operator =="**":
    print(number1**number2)
elif operator =="%":
    print(number1%number2)



for i in range(0,21):
    print(i)
num=0
while num<=20:
    print(num)
    num+=1

for i in range(1,11):
    print(3*i)

for i in range(1,11,2):
    print(3*i)



num=1
while num<=10:
    print(3*num)
    num+=2



for num in range(1,11):
    if 2*num==10:
        break
    print(2*num)


num=1
while num<=10:
    if 2*num==14:
     num+=1
     continue
    print(2*num)
    num+=1

for i in range(1,11):
   print(i)


for i in range(2,20,2):
   print(i)

for i in range(1,21,2):
   print(i)

   

name= "Rishabh"
age= 18


marks=int(input("Enter Marks"))
if marks>90:
    print("a")
elif marks>80:
    print("b")
elif marks>70:
    print("c")

    
n=int(input("Enter Number"))
if n%2==0:
    print("even")
else :
    print("odd")

for i in range(1,101):
   if i%2==1:
      continue
   print(i)

   
n=int(input("Fill number: "))
for i in range(2,n):
   if n%i==0:
      print("Not prime")
      break
else :
   print("Prime")


num1=23
num2=25
def addition(num1,num2):
    result=num1+num2
    print(result)

addition(23,25)


def Greet(state):
    print("Good_Morning",state)

Greet("Uttar Pradesh")


def odd_even(number):
    if number%2==0:
        print("This number is even")
    else:
        print("this no. is odd")

odd_even(2)


def multiplication(num1,num2):
    result=num1*num2
    return result

a=multiplication(23,15)
print(a)



def factorial(number):
    factorial=1
    for n in range(1,number+1):
        factorial=factorial*n

    return factorial

print(factorial(6))


def sum1():
    sum=0
    for n in range(1,11):
       sum=sum+n

    return sum

print(sum1())


def sum():
    number=0
    for i in range(1,11):
        if i%2==1:
         number=number+i

    return number
print(sum())



def sum(num):
   if num==0:
      return 0
   return num+sum(num-1)
print(sum(10))


def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return fib(num-1)+fib(num-2)
print(fib(8))

#for get or find fabbonaci series.
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return fib(num-1)+fib(num-2)

for i in range(14):
    print (fib(i))

def count_arg(*a):
    count_v=0
    for num in a:
        count_v+=1
    return count_v
print(count_arg(21,31,41,51,61))
 

n=121
temp=n
rev=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp//=10
if n==rev:
    print("palindrome")
else:
    print("not ")


name="Oreo"
name1=" "
for i in name:
    name1=i+name1
print(name1)
    
"""
"""
name="Rishabh"
print(name.isalpha())
#True
"""
"""
name="Rishabh324"
print(name.isalnum())
#True
"""
"""
name="Ranu pratap bhanu"
print(name.isnumeric())
#false
"""
"""
name="3425"
print(name.isnumeric())
#True
"""
"""
name="Lala Lajpat Ray"
print(name.split())
#['Lala', 'Lajpat', 'Ray']
"""
"""
name="Ram Chandra"
print(len(name))
"""
"""
name="   Ranu Singh  "
print(name.strip())
"""
"""
name="Saurabh Kumar Nayak"
count=0
for i in name:
    count+=1
print(count)
#19
"""
"""
name="Saurabh Kumar Nayak"
count=0
for i in name:
   if i!=" ":
     count+=1
print(count)
#17
"""
"""
name="Saurabh Kumar Nayak"
count=0
for i in name:
   if i in "aeiou":
     count+=1
print(count)
#vowels=7
"""
"""
name="Saurabh Kumar Nayak"
count=0
for i in name:
   if i not in "aeiou":
     count+=1
print(count)
#consonants=12
""" 
"""
name="Saurabh Kumar Nayak"
count=0
for i in name:
   if i not in "aeiou" " ":
     count+=1
print(count)
#consonants=10
"""
"""
name="Rahul"
count=0
for i in name:
   if i =="h":
      break
   count+=1
print(count)
#index=2
"""
"""
print(ord("A"))
#ascii value 65
"""
"""
name="python"
for i in name:
    result=chr(ord(i)-32)
    print(result,end=" ")
#PYTHON
"""
"""
name="I am Ravi Kishan Money Follows Paisan"
largest=0
word=0
for i in name:
    if i!=" ":
       word=word+1
    elif i==" ":
       if largest<word:
          largest=word
          word=0
       else:
        word=0
if word>largest:
   largest=word
print(largest)
#7
"""


"""
name="i am 24"
for i in name:
    if i.isnumeric():
        print(i,end=" ")
#24
"""
"""
name="I am Ravi Kishan Money Follows Paisan"
largest=""
word=""
for s in name:
    if s!=" ":
        word+=s
    elif s==" ":
        if len(word)>len(largest):
            largest=word
            word=""
        else:
            word=""
if len(word)>len(largest):
    largest=word
print(largest)
#Follows
"""
"""
list1=[32,16,26,76,97]
count=0
for i in list1:
    if i>count:
        count=i
print(count)
#97
"""
"""
list1=[32,16,26,76,97]
count=list1[0]
for i in list1:
    if i<count:
        count=i
print(count)
"""
"""
num=[20,34,43,33,65,90,54]
count=0
for i in num:
   if i%2==0:
      count+=i
print(count)
"""
"""
num=[20,34,43,33,65,90,54]
largest=0
second=1
for i in num:
   if i>largest:
      second=largest
      largest=i
   elif i>second and i!=largest:
      second=i
print(second)
"""
"""
section=[12,34,70,2,8,33,67]
numbers=[x*10 for x in section if x%2==0]
print(numbers)
number=[x**2 for x in section if x%2==1]
print(number)
""" 
"""
none=[12.89,88,72,92]
num=[x if x%2==1 else"Nonu hua hua" for x in none]
print(num)
"""
"""
number=[25,62,43,47,77]
num=[x if x%2==0 else x*4 for x in number]
print(num)
"""
"""
list1=[[12,24,36],[17,51,85],[69,115,161]]
print(list1[0])
"""
"""
name=["Shresth","Mahima","Hanshita","Aryan","Gauri"]
print(sorted(name))
"""
#a=0
#print(bool(a))

#a=""
#print(bool(a))

#x=" "
#if x:
 #   print("x")
#else:
 #   print("y")

#x=""
#if x:
 #   print("x")
#else:
 #   print("y")

#x= None
#if x:
 #   print("x")
#else :
 #   print("y")
 
"""
num=(1,2,3,4,5,6,8,9)
excepted_num=0
real_num=0
for i in range(1,10):
     excepted_num+=i

for j in num:
     real_num+=j
print(excepted_num-real_num)
#7
"""
"""
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
for i in days:
    print(i)

#monday
tuesday
wednesday
thursday
friday
saturday
sunday
"""

#days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
#print(days.index("wednesday"))

#days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
#print(days.count("saturday"))
"""
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
b,*a=days
print(b,*a)
#List(monday tuesday wednesday thursday friday saturday sunday)
"""
"""
num=[4,7,8,1,2]
target=10
for i in num:
    for j in num:
        if i+j==10:
         print(i) or print(i,j)
         #8,2     or #8,2
                      2,8
"""
"""
num=[121,131,141,151,161]
for i in range(5//2):
    num[i],num[len(num)-1-i]=num[len(num)-1-i],num[i]
print(num)
#[161, 151, 141, 131, 121]
"""
"""
A={12,14,54,67,67,87}
B={12,14,54,67,67,87}
print(A.issubset(B))
"""
"""
a={97,89,45,76}
b={97,89,45,76,87,90,87,67}
print(b.issuperset(a))
"""
"""
a={32,23,54,77,98}
b={32,23,54,77,98}
print(a.isdisjoint(b))
"""
"""
dict1={"name":"rishabh","price":"100000"}
print(dict1)
print(dict1["roll_number"])
print(dict1.get("name"))
"""
"""
dict1={"name":"rishabh","price":"100000"}
print(dict1.get("roll_no","Not intrested"))
"""
"""

dict1={"name":"rishabh",#tuple_vlue
       (12,75,12):"100000"}
print(dict1)
"""
"""
dict1={"name":"rishabh","price":"100000"}
dict1.update({"class":"12","add":"lucknow"})
print(dict1)
"""
"""
dict1={"name":"rishabh","price":"100000"}
for i in dict1:
    print(i,dict1[i])
print(dict1)
"""
"""

dict1={"name":"rishabh","price":"100000"}
for i in dict1:
    print(i,dict1[i])
print(dict1.keys())
"""
"""
dict1={"name":"rishabh","price":"100000"}
for i in dict1 values:
    print(i)
"""
"""
dict1={"name":"rishabh","price":"100000"}
for i in dict1:
    print(i,dict1[i])
"""
"""
dict1={"name":"Narendra","desgination":"PM","hobby":"loving country","friend":"Putin"}
for i in dict1.values():
    print(i)
"""
"""
dict1={"name":"Narendra","desgination":"PM","hobby":"loving country","friend":"Putin"}
for i in dict1.keys():
    print(i)
"""
"""

dict1={"name":"Narendra","desgination":"PM","hobby":"loving country","friend":"Putin"}
for i in dict1.keys():
   for j in dict1.values():
    print(i,j)
"""
"""
dict1={"name":"Narendra","desgination":"PM","hobby":"loving country","friend":"Putin"}
print(dict1.pop("friend"))
print(dict1)
"""
"""
dict1={"name":"Narendra","desgination":"PM","hobby":"loving country","friend":"Putin"}
print(dict1.popitem())
"""
"""
dict1={"students1":{"name":"shresth","class":1},"students2":{"name":"Raj","class":3}}
print(dict1)
"""
"""
name=[1,2,3,4,5]
dict1={x:x*2 for x in name}
print(dict1)
"""
"""
roll_num=[1,2,3,4,5,6]
name=["rahul","gaurav","ranu","harsh","nandu","mr been"]
dict1={i:y for i,y in zip(roll_num,name)}
print(dict1)
"""
"""
name=["rahul","gaurav","ranu","harsh","nandu","mr been"]
print(dict.fromkeys(name,"no value")
"""
"""
name=["12","23","34","45"]
#map(function_iterable)
int_num=map(lambda x:int(x)*2,name)
print(list(int_num))
#[24, 46, 68, 90]
"""
"""
name=["12","23","34","45"]
int_num=map(int,name)
print(list(int_num))
#[12, 23, 34, 45]
"""
"""
square=lambda x:x**2
print(square(5))
#25
"""
"""
square=lambda x:x+x
print(square(8))
#16
"""
"""

name=["12","23","34","45"]
int_num=list(map(int,name))
even=list(filter(lambda x:x>30,int_num))
print(even)
#[34, 45]
"""
"""
name=["12","23","34","45"]
int_num=list(map(int,name))
from functools import reduce
sum_list=reduce(lambda x,y:x+y,int_num)              
print(sum_list)
#114

"""
"""
class Student:
    def study():
        print("studying")

s1=Student()
print(s1)
"""
"""
dict1={"Rishabh":12,"Ranu":13,"Rahul":14,"Ranjeet":57,"Ramesh":45,"Ravi":33,"Rohan":28,"Rakesh":19,"Ramesh":45}
marks=[sorted(dict1.items(), key=lambda x: x[1])]
print(marks)
#[('Rishabh', 12), ('Ranu', 13), ('Rahul', 14), ('Rakesh', 19), ('Rohan', 28), ('Ravi', 33), ('Ramesh', 45), ('Ramesh', 45), ('Ranjeet', 57)]

"""
"""

dict1={"Rishabh":12,"Ranu":13,"Rahul":14,"Ranjeet":57,"Ramesh":45,"Ravi":33,"Rohan":28,"Rakesh":19,"Ramesh":45}
marks=[sorted(dict1.items(), key=lambda x: x[1], reverse=True)]
print(marks)
#[('Ranjeet', 57), ('Ramesh', 45), ('Ramesh', 45), ('Ravi', 33), ('Rohan', 28), ('Rakesh', 19), ('Rahul', 14), ('Ranu', 13), ('Rishabh', 12)]

"""
"""
dict1={"Rishabh":12,"Ranu":13,"Rahul":14,"Ranjeet":57,"Ramesh":45,"Ravi":33,"Rohan":28,"Rakesh":19,"Ramesh":45}
marks=list(filter(lambda x: x[1] < 50, dict1.items()))
print(marks)
#[('Rishabh', 12), ('Ranu', 13), ('Rahul', 14), ('Rakesh', 19), ('Rohan', 28), ('Ravi', 33), ('Ramesh', 45)]

"""
"""
dict1={"Rishabh":12,"Ranu":13,"Rahul":14,"Ranjeet":57,"Ramesh":45,"Ravi":33,"Rohan":28,"Rakesh":19,"Ramesh":45}
marks=list(map(lambda x:"even" if x%2==0 else "odd", dict1.values()))
print(marks)
#['even', 'odd', 'even', 'odd', 'odd', 'odd', 'even', 'odd', 'odd']

"""
"""
name=list("Rishabh")
name=tuple("Rishabh")
name=set("Rishabh")
print(name)
#['R', 'i', 's', 'h', 'a', 'b', 'h']

"""
"""
         #class in python
class Student:
    school_name="APPS School"
            #Constructor 
    def __init__(self,name,age,class_name,roll_nu,marks):
                #attributes 
        self.name=name
        self.age=age
        self.class_name=class_name
        self.roll_nu=roll_nu
        self.marks=marks

            #create object
s1=Student("Rishabh",18,"12th",12,100)
s2=Student("Ranu",19,"12th",13,90)
s3=Student("Rahul",20,"12th",14,80)
Student.school_name="APPS School Lucknow"
print(s2.school_name)
print(s1.school_name)
s1.roll_nu=15
print(s1.roll_nu)

"""
"""
class Hospital:
    hospital_name="KGMU hospital"
                #constructor
    def __init__(self,patient_name,age,gender,doctor_name,room_no):
               #attributes
        self.patient_name=patient_name
        self.age=age
        self.gender=gender
        self.doctor_name=doctor_name
        self.room_no=room_no
                #inheritance object
    def display(self):
        print("Hospital Name:",self.hospital_name)
        print("Patient Name:",self.patient_name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Doctor_name",self.doctor_name)
        print("Room_no:",self.room_no)
        
    def check_result(self):   
        if self.age<18:
            print("Offer")
        else:
            print("Not offer") 
                #object
s1=Hospital("Anurag",25,"Male","Dr.Ramesh",101)
s2=Hospital("Ramesh",30,"Male","Dr.Rahul",102)
s3=Hospital("Ravi",35,"Male","Dr.Ranu",103) 
print(s1.patient_name,s1.age,s1.gender,s1.doctor_name,s1.room_no)   
print(s2.patient_name,s2.age,s2.gender,s2.doctor_name,s2.room_no)   
print(s3.patient_name,s3.age,s3.gender,s3.doctor_name,s3.room_no)
print(s1.check_result())

"""
"""


class ATM:
    def __init__(self,account_number, pin,ifsc,balance):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        self.ifsc=ifsc
    def bank_balance(self):
        return f"Your bank balance is: {self.__balance}"

    def deposit(self, value):
        self.__balance = self.__balance + value
        return self.__balance
    def withdraw(self, value):
            self.__balance=self.__balance-value
            return self.__balance
p=ATM(1234567890, 1234, "IFSC001", 50000)
print(p.bank_balance())
print(p.deposit(10000))
print(p.withdraw(10000))
"""
"""
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks=marks
    def show_marks(self):
        return f"{self.__marks}"

    def update_marks(self,updated_marks):
        self.__marks=self.__marks+updated_marks
        return f"updated_marks is {self.__marks}"

s1=Student("Rishabh",100)
s1.__marks=80
print(s1.__marks)
print(s1.show_marks())
print(s1.update_marks(5))
print(s1._Student__marks)
"""
"""
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks=marks
    @property
    def show_marks(self):
        return f"{self.__marks}"
    @marks.setter
    def marks(self,updated_marks):
        if updated_marks<0 and updated_marks>100:
            self.__marks=updated_marks
            return f"updated_marks is {self.__marks}"
        else:
            return f"(invalid marks)"

s1=Student("Rishabh",100)
s1.__marks=80
print(s1.__marks)
print(s1.show_marks())
print(s1.update_marks(5))
print(s1._Student__marks)
"""
"""
class Office:
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.__salary=salary
    @property
    def show_salary(self):
        return f"Your salary is {self.__salary}"
    @show_salary.setter
    def show_salary(self,updated_salary):
        if updated_salary>0 and updated_salary<=100000:
            self.__salary=self.__salary+updated_salary
            return f"updated salary is{self.__salary}"

s1=Office("Gaurav","HR",45000)
s1.show_salary=90000
print(s1.show_salary)
"""
"""
class Office:
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.__salary=salary
    def show_Salary(self):
        return f"Your salary is {self.__salary}"
    def show_salary(self,updated_salary):
            self.__salary=self.__salary+updated_salary
            return f"updated salary is_{self.__salary}"
s1=Office("Gaurav","HR",45000)
print(s1.show_Salary())
print(s1.show_salary (10000))

"""
"""
       #Single Inheritance
class Animal:  #(Parent class)
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
class Dog(Animal):   #(child class)
    def __init__(self,name,age,color,breed):
        super(). __init__(name,age,color)
        self.breed= breed
d=Dog("Hii",12,"black","Mudhol")
print(d.name)
print(d.breed)
print(d.age)
"""
"""
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Waling")

class Dog(Mammal):
    def bark(self):
        print("Barking")
d=Dog()
print(d.walk)
"""
"""
class Father:
    def Papaji(self):
        print("Papa ki property")
class Mother(Father):
    def Mummy (self):
        print("Mummy ki property")
class Me(Mother):
    def meri(self):
        print("Sari property meri")

m=Me()
m.Mummy()
m.Papaji()
"""
"""
class Grandfather:
    def __init__(self,land):
        self.land=land
class Father(Grandfather):
    def __init__(self,land):
        super().__init__(land)
class Beta(Grandfather):
    def __init__(self,land):
        super().__init__(land)
s=Beta("20 crore ka makan")
print(s.land)
"""
"""
class Father:
     def __init__(self,land):
         self.land=land
     def papaji(self):
         print("papa di property")
class Mother:
     def __init__(self,Jewellery):
         self.Jewellery=Jewellery
     def mataji(self):
        print("mataji di property") 
class Son(Father,Mother):
     def __init__(self, land,Jewellery,car,house):
         Father.__init__(self,land)
         Mother.__init__(self,Jewellery)
         self.car=car
         self.house=house
my=Son(3,"Necklace","Tata Sierra","2BHk Flat")
print(my.land)
"""
"""
class Payment:
    def pay(self):
        print("Payment in progress")
class Upi(Payment):
    def pay(self):
        print("Payment with Upi")
class Debit(Payment):
    def pay(self):
        print("Pay with Debit Card")
class Net_Banking(Payment):
    def pay(self):
        print("Payment With Net_Banking")
p=Debit()
p.pay()
p=Net_Banking()
p.pay()
p=Upi()
p.pay()

"""
"""
class Email:
    def send(self):
        print("Notify through Email")
class Whatsapp:
    def send(self):
        print("Notify through whatsapp")
class Sms:
    def send(self):
        print("Notify through Sms")

notify=[Email(),Whatsapp(),Sms()]
def make_notification(notify):
    for i in notify:
        i.send()

make_notification(notify)
"""
"""

from abc import ABC,  abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        print("Payment in progress")
class Upi (Payment):
    def pay(self):
        print("Payment with Upi App")
class Debit(Payment):
    def pay(self):
        print("Pay through Debit Card")
class Navi(Payment):
    def pay(self):
        print("Payment in progress")
    def hii(self):
        print("Payment success")
p=Navi()
print(p.hii())

"""
"""
class Worker:
    Company_name="Furniture"
    def __init__(self,name,age,address,id):
        self.name=name
        self.age=age
        self.address=address
        self.id=id
    @classmethod
    def Company_change(cls,Company_name):
        cls.Company_name=Company_name
        return cls.Company_name
print(Worker.Company_change("CMS"))    
print(Worker.Company_name)
"""
"""
class Center:
    @staticmethod
    def format_name_id(number):
        return f"name_id{number:1>3d}"
    
print(Center.format_name_id( 36))
"""
"""
class Employee:
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return f"Employee name is {self.value}"
s=Employee("Ritik")
print(s)
"""
"""
class Employee:
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return f"Employee name is {self.value}"
    def __len__(self):
        return len(self.value)
s=Employee("Ritik")
print(s)
print(len(s))
"""
"""
class Employee:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        result=self.value + other.value
        return result
s=Employee(10)
r=Employee(30)
print(r+s)
"""
"""
class Student:
    school_name="APPS"
    def __init__(self,name,age,std,subject,add):
        self.name=name
        self.age=age
        self.std=std
        self.add=add
        self.subject=subject
    def display_info(self):
        print("age",self.age)
        print("std",self.std)
        print("subject",self.subject)
        print("add",self.add)
r=Student("Ritik",22,"BA","maths","budheswar in Lucknow")
g=Student("Gaurav",17,10,"Science","Sandila")
s=Student("Saurabh",20,"Graduated","Art","From MP")
s.display_info()
r.display_info()
g.display_info()
"""
"""
class Employee:
    Company_name="HCL.Com"
    def __init__(self,name,age,mob_no,salary,add,dept):
        self.name=name
        self.age=age
        self.mob_no=mob_no
        self.salary=salary
        self.add=add
        self.dept=dept
    def display_info(self):
        print("name",self.name)
        print("age",self.age)
        print("mob_no",self.mob_no)
        print("salary",self.salary)
        print("add",self.add)
        print("dept",self.dept)
    def update_salary(self,value):
        new_salary=self.salary+value
        return new_salary
    def update_dept(self,new_dept):
        self.dept=new_dept
        return self.dept
o=Employee("Om",40,5214789632,20000,"Lucknow","Dealer")
a=Employee("Anurag",26,7894563210,17000,"Laalbag","HR")
h=Employee("Harsh",34,4587963210,15000,"GomtiNagar","IT")
k=Employee("Kuldeep",40,8521479630,18000,"Para","Marketing")
m=Employee("Mohit",33,7896541330,16000,"Hardoi","Editor")
j=Employee("jakariya",44,5896587412,17000,"Sitapur","Artist")
a.display_info()
h.display_info()
k.display_info()
m.display_info()
j.display_info()
print(h.update_salary(20000))
o.display_info()
"""
"""
class Employee:
    def __init__(self, name, emp_id, department, salary, designation):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        self.designation = designation
    def display_details(self):
        print(f"ID:{1}  Name:{"Ayush"}  Role:{"HR Manager"}  Dept:{"HR"}  Salary:{70000}")

    def calculate_salary(self, bonus=0):
        total_pay = self.salary + bonus
        return total_pay

    def update_department(self, new_department):
        self.department = new_department
        print(f"-> {"Ayush"}'s dept updated in {"IT"}.")


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employee_list = [] 

    def add_employee(self, employee):
        self.employee_list.append(employee)
        print(f"Added {employee.name} to the {self.dept_name} department.")

    def remove_employee(self, emp_id):
        for emp in self.employee_list:
            if emp.emp_id == emp_id:
                self.employee_list.remove(emp)
                print(f"Removed employee ID {emp_id} from {self.dept_name}.")
                return
        print(f"Employee ID {emp_id} not found.")

    def get_total_payroll(self):
        total_payroll = sum(emp.salary for emp in self.employee_list)
        return total_payroll

if __name__ == "__main__":
 emp1 = Employee("Rahul", 101, "HR", 75000, "Engineer")
 emp2 = Employee("Bablu", 102, "Sales", 82000, "Developer")
it_dept = Department("IT")
print("Add Employees")

it_dept.add_employee(emp1)
it_dept.add_employee(emp2)
print("Employee Details")
for emp in it_dept.employee_list:
    emp.display_details()

print(f"Total Payroll for {it_dept.dept_name}: {it_dept.get_total_payroll()}")
print("Transfer Employee")
emp1.update_department("AI Engineer")
print(f"Rahul's total pay with a 5,000 bonus: {emp1.calculate_salary(5000)}")

"""
"""
import time

def add_decor(func):
    def wrapper(*args):
        print("function is going to start")
        time.sleep(2)
        print(func(*args))
    return wrapper

@add_decor
def name(name,class_name):
    return f"Hello {name},you are in class {class_name}"
def add(a,b):
    return a+b
print(add(10,20))
print(name("Arnav", "10th"))
"""
