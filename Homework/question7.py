#what is faster list or tuple?
#Tuples are allocated in the single block and are immutable and does not require extra storage
#Lists are allocated in double block, one is of fixed length and storage and other is of variable length and storage

tuple1 = (1,2,3,4,5)
print(tuple1)

list1 = [1,2,3,4,5]
print(list1)
list1.append(6)
print(list1)