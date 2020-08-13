#what are filters in python?


def function1(x):
    return x**2

filter1 = filter(function1,[1,2,3,4,5])

for number in filter1:
    print(number)