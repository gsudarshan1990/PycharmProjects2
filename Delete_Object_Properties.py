class Person:
    def __init__(self,fname,age):
        self.firstname=fname
        self.age=age

    def printname(self):
        print("Hello"+self.firstname+" age",self.age)

x1=Person("John",29)
x1.printname()

del x1
