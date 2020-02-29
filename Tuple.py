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

