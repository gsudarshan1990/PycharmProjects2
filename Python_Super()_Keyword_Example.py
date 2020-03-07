#Python has a Super() function that will make the child class inherit all the methods and properties from its parent


#By using the super() function, you need have to use the name of the parent element,

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x=Student('Shashank',"Deepu")
x.printname()


#Add Properties in the Child Class

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname+"    "+self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduation=2011

x=Student('Shashank','Deepu')
x.printname()
print(x.graduation)

#Add Methods

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname+"   "+self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

    def new_method(self):
        print('This class is used adding new methods')

x=Student('Shashank',"Deepu")
x.printname()
x.new_method()

