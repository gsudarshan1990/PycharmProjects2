def my_function():
    print("Hello from a function")

my_function()

def my_function(fname):
    print(fname+"Acquinson")

my_function("sudarshan")
my_function("Jeeba")
my_function("Joya")

def my_function(country="Norway"):
    print("I am from "+country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
my_function(fruits)

def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function(child3,child2,child1):
    print("The Youngest Child is "+child3)

my_function(child1="Eme",child2="Yip",child3="Ben")


def my_function(*kids):
    print(kids[2])

my_function("Jim","Toe","Harry")

def myfunction():
    pass