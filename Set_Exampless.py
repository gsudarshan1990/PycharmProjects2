thisset={"Java","Python","Ruby","Selenium"}
print(thisset)

thisset={"Java","Python","Ruby","Selenium"}
for x in thisset:
    print(x)


thisset={"Java","Python","Ruby","Selenium"}
print("Java" in thisset)

thisset={"Java","Python","Ruby","Selenium"}
thisset.add("Hadoop")
print(thisset)


thisset={"Java","Python","Ruby","Selenium"}
thisset.update(["BDD","AWS"])
print(thisset)

thisset={"Java","Python","Ruby","Selenium"}
print(len(thisset))

thisset={"apple","banana","cherry"}
thisset.remove("apple")
print(thisset)

thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x)

print(thisset)

thisset={"apple","banana","cherry"}
thisset.clear()
print(thisset)



set1={"a","b","c"}
set2={1,2,3}

set3=set1.union(set2)
print(set3)

set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)