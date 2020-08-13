#How do you raise the exception?


def function1(a):
    if type(a) == int:
        print(a)
    else:
        raise ValueError('Number is not interger')

function1('a')