#What is the purpose of the userdict in python

#userdict is a class wrapper for the dictionary object
from collections import UserDict

dict1 = {'a':1, 'b':2, 'c':3}

userd = UserDict(dict1)
print(userd)



dict2 = {}

userd2 = UserDict(dict2)
print(userd2)


class Mydict(UserDict):
    """This is a user defined dictionary"""
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    def pop(self, k=None):
        raise RuntimeError("Deletion not allowed")

    def popitem(self):
        raise RuntimeError("Deletion not allowed")

a = {'a':1,'b':2,'c':3}
d = Mydict(a)

print(d)
#d.pop('a')