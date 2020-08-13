#How do we add values in the array?


#Array hold only fixed number of values and cannot be extended

from array import array

a = array('i',[1,2,3,4,5])
print(a)

a.insert(5,6)
print(a)

