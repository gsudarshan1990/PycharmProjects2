#Constructors are of two types


#Creating Multiple Objects
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name %s ange age %d"%(self.name,self.age))

emp1=Employee("John",101)
emp2=Employee("David",102)
emp3=Employee("Krithika",900)

emp1.display()
emp2.display()
emp3.display()

#Non Parameterized Constructor

class Student:
    def __init__(self):
        print("This is non parameterised constructor")

s=Student()

#Count the number of Objects creation

class Student:
    count = 0
    def __init__(self):
       Student.count=Student.count+1

s1=Student()
s2=Student()
s3=Student()
s4=Student()
s5=Student()
s6=Student()

print("The number of objects created is %d",Student.count)


#Parameterized Constructor
class Student:
    def __init__(self,name):
        print("This is the parameterized constructor")
        self.name=name
    def show(self):
        print("Hello",self.name)

student=Student("John")
student.show()