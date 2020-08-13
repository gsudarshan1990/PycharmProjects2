#what is the use of If, Not and In statement


#If is used to check the condition

list1 = [i for i in range(10)]

for num in list1:
    if num%2 == 0:
        print('even number %d'%num)

#in is used to check whether a variable is present
print(2 in list1)
#not in is used to check whether a variable is not present

print(2 not in list1)


