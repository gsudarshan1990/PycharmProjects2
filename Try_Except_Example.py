#Sample try and except block

try:
    print(x)
except:
    print("An exception has occured")


try:
    print(x)
except NameError:
    print("Variable X is not defined")
except:
    print("Something also went wrong")

try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("Try except is finished")