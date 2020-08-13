#what is the use local and global variables


b =4
def function1():
    a = 2
    print(a)
    b = 3
    print(b)
    print('Here "a" is a local variable')
    print('Here "b" is a global variable')

def function2():
    print(b)

function1()
function2()