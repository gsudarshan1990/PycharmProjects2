x="Prem"

def myfunc():
    print("My Name is "+x)

myfunc()

def myfunc():
    global x
    x="fanstatic"

myfunc()
print("Python is "+x)

x="awesome"

def myfunc():
    global x
    x="fantastic"

myfunc()

print("Python is "+x)
