#what is namedtuple in python?
#namedtuple is a tuple which field name which acts as a key

from collections import namedtuple

employee = namedtuple('Employee',['name','age','salary'])
employee1 = employee('sonu',30,'2000')
employee2 = employee('deepu',31,'50000')
print(employee1)
print(employee2)


