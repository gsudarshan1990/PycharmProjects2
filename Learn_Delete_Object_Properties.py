class Person:
    def __init__(self,fname,age):
        self.firstname=fname
        self.age=age

    def printname(self):
        print("Hello"+self.firstname+"  age:",self.age)

p1=Person("John",29)

p1.printname()

del p1.age

print(p1.age)