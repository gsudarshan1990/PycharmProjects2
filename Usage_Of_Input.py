#Sum of the numbers used via the input

def sum_of_numbers():
    sum=0
    while True:
        num=int(input("Enter the number , 0 to quit"))
        if num == 0:
            break
        sum=sum+num
    return sum

print(sum_of_numbers())

#Adding of the numbers to the list obtained via the list

def list_appending():
    list1=[]
    while True:
        num=int(input("Enter the number to append to the list and 0 to quit"))
        if num == 0:
            break
        list1.append(num)
    return list1

print(list_appending())
