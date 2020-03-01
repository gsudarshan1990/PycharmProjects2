#Printing the Class Name
class Myclass:
    x=5

print(Myclass)

class Myclass:
    x=5

obj1=Myclass()
print(obj1.x)

#Usage of the init constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunction(self):
        print(self.name)
        print(self.age)

p1=Person("sudarshan",29)
p1.myfunction()


#We need not necessarily use only self key and we can also use other keys

class Person:
    def __init__(obj,name,age):
        obj.name=name
        obj.age=age

    def myfunction(abc):
        print(abc.name)
        print(abc.age)

p1=Person("sudarshan",29)
p1.myfunction()

#Modify the object properties

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print('name is'+self.name+' age is: '+str(self.age))


p1=Person("Govindarajan",58)
p1.myfunc()
p1.age=60
p1.myfunc()
