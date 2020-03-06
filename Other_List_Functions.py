mylist1=["a","b","c"]
mylist2=[1,2,3]

list2=mylist1+mylist2
print(list2)

mylist3=["a","b","c"]
mylist4=[1,2,3]

mylist3.extend(mylist4)
print(mylist3)

#Usage of the Sublists
newEngland=[["Massachusetts",6992824],["Connecticut",359608],["Maine",1328302],["New Hampshire",1323459],["Rhode Island",1051511],["Vermont",626630]]
midatlantic=[["New York",1976422],["New Jersey",8938175],["Pennsylvania",12787209]]


def report(list_sample):
    print("State"+"                        "+"Population")
    for list1 in list_sample:
        print(list1[0]+"          ",list1[1])

report(newEngland)
print()
print()
print()

print("====================")

report(midatlantic)

#Calculate the population of the new england
def calculate_population(list1):
    total_states=len(list1)
    sum_population=0
    for item_list in list1:
        sum_population=sum_population+item_list[1]
    print('The total states ',total_states)
    print('The population of the total states',sum_population)

calculate_population(newEngland)


list1=['a','b','c','d']
list2=['c','d',7,'c']

def create_list(list1,list2):
    list4=[]
    for item1 in list1:
        list3 = []
        for item2 in list2:
            if (item1 == item2):
                list3.append('*')
            else:
                if  isinstance(item1,str):
                    if isinstance(item2,str):
                        str3=item1+item2
                        list3.append(str3)
                    else:
                        str4=str(item2)
                        str5=item1+str4
                        list3.append(str5)
                        print(list3)
        list4.append(list3)
    return list4

print(create_list(list1,list2))


#Average of numbers
def average_list(list1):
    sum=0
    total_count=len(list1)
    for num in list1:
        sum=sum+num
    average=(sum)/total_count
    return average

numlist1=[65,44,3,56,48,74,7,97,95,42]
numlist2=[4,6,8,12,2,7,19]

print(average_list(numlist1))
print(average_list(numlist2))