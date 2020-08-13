#How do we create a class in python? What is a class in Python?

#class contains the attributes and function which works on the attributes. Objects are created which are the instance of the class
#class are used to represent the real world objects

class Table:
    """This class desribes the table"""
    def __init__(self):
        """This is used to initialize the value"""
        self.wood = 'Neem wood'
        self.color = 'blue'
        self.purpose = 'study'

t = Table()
print(t.wood)
print(t.color)
print(t.purpose)