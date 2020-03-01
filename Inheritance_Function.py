#Defination of the Class
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def print_name(self):
        print(self.firstname)
        print(self.lastname)

x=Person("Sudarshan","Govindarajan")
x.print_name()


#Inheritance with Pass Keyword
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def print_name(self):
        print(self.firstname)
        print(self.lastname)


class Student(Person):
    pass

s=Student("Sudarshan","Govindarajan")
s.print_name()


#Inheritance with the __init__ function
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def print_name(self):
        print(self.firstname)
        print(self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

s=Student("Sudarshan","Govindarajan")
s.print_name()

