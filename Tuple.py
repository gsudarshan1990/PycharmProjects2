mytuple=("Harry","John","Ben")
print(mytuple)

print(mytuple[1])

mytuple=("Harry","John","Ben","Dorian","Obenza","kenny")
print(mytuple[2:5])

print(mytuple[-4:-1])



mytuple=("Harry","John","Ben","Dorian","Obenza","kenny")
list1=list(mytuple)
list1[1]="Yep"
newtuple=tuple(list1)
print(newtuple)

mytuple=("Harry","John","Ben","Dorian","Obenza","kenny")
for x in mytuple:
    print(x)

mytuple = ("Harry", "John", "Ben", "Dorian", "Obenza", "kenny")
if "John" in mytuple:
    print("Yes")

mytuple = ("Harry", "John", "Ben", "Dorian", "Obenza", "kenny")
print(len(mytuple))

tuple1=(1,2,3)
tuple2=('a','b','c')

tuple3=tuple1+tuple2

print(tuple3)




tuple2=("apple","mango","orange")
del tuple2
print(tuple2)


tup1=(2,3)
print(tup1)

tup3=(3,4,5)
print(tup3)

tup4=('a','b')
print(tup4)

tup5=("Morning","Afternoon","Evening")
print(tup5)

tup=('a','e','i','o','u')
print(tup)
print(tup[1])
print(tup[2])
print(tup[0])
print(tup[-1])
print(tup[3:4])
print(tup[:5])
print(tup[3:])

