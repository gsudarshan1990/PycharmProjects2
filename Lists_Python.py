mylist=["Anusha","Chelvi","Mythili"]


print(mylist)

print(mylist[1])

print(mylist[-1])

#Accessing the list via Slicing
mylist=["Anusha","Chelvi","Mythili","Nithya","Arun","Vaishnavi"]
print(mylist[-1])
print(mylist[2:5])

#Change the value of the list
mylist[1]="Banu"
print(mylist)

if "Anusha" in mylist:
    print("Yes, Anusha exists")

print(len(mylist))

mylist.append("Surya")

print(mylist)

mylist.insert(2,"Eme")
print(mylist)
mylist=["Anusha","Chelvi","Mythili","Nithya","Arun","Vaishnavi"]

mylist.remove("Chelvi")

print(mylist)


print("=====================")
mylist1=["Anusha","Chelvi","Mythili","Nithya","Arun"]
mylist1.pop()

print(mylist1)

print(mylist1)


def count_a(list1):
    count=0
    for lis in list1:
        if 'a' == lis:
            count=count+1
    print("Total number of 'a' in the list is : ",count)



lis1=['a','b','a','r','c','a','a']

count_a(lis1)

def average(list0):
    length=len(list0)
    sum=-1
    for number in list0:
        sum=sum+number
    number_average=(sum/length)
    return number_average

nlis=[1,4,8,105,210,-3,41,8,33,1]
rlis=[3.14,7.26,-4.76,0,8.24,9.1,-100.7,4]
print(average(nlis))
print(average(rlis))

def iterating_list(list1):
    for item in list1:
        print(item)

newEngland=["Maine","New Hampshire","Vermont","Rhodes Island","Massachussets","Connecticut"]

iterating_list(newEngland)




