"""
Problem 2_4:
random.random() generates pseudo-random real numbers between 0 and 1. But what
if you needed other random reals? Write a program to use only random.random()
to generate a list of random reals between 30 and 35. This is a simple matter
of multiplication and addition. By multiplying you can spread the random numbers
out to cover the range 0 to 5. By adding you can shift these numbers up to the
required range from 30 to 35.  Set the seed in this function to 70 so that
everyone generates the same random numbers and will agree with the grader's
list of random numbers. Print out the list (in list form).
"""


import random

def problem4():
    random_number=random.random()
    rand_int=random.randint(0,5)
    initial_random_number=rand_int*random_number
    final_random_number=initial_random_number+30
    print(final_random_number)

for i in range(10):
    problem4()

"""
Let's do a small simulation. Suppose that you rolled a die repeatedly. Each 
time that you roll the die you get a integer from 1 to 6, the number of pips
on the die. Use random.randint(a,b) to simulate rolling a die 10 times and 
printout the 10 outcomes. The function random.randint(a,b) will
generate an integer (whole number) between the integers a and b inclusive.
Remember each outcome is 1, 2, 3, 4, 5, or 6, so make sure that you can get 
all of these outcomes and none other. Print the list, one item to a line so that
there are 10 lines as in the example run.  Make sure that it has 10 items 
and they are all in the range 1 through 6.  Here is one of my runs. In
the problem below I ask you to set the seed to 171 for the benefit of the 
auto-grader. In this example, that wasn't done and so your numbers will be 
different.  Note that the seed must be set BEFORE randint is used.  
number=random.randint(1,6)
"""

def problem5():
   for i in range(10):
       number = random.randint(1, 6)
       print(number)

problem5()

"""
Let's continue with our simulation of dice by rolling two of them. This time
each die can come up with a number from 1 to 6, but you have two of them. The
result or outcome is taken to be the sum of the pips on the two dice. Write a 
program that will roll 2 dice and produce the outcome. This time let's roll 
the two dice 100 times. Print the outcomes one outcome per line.
"""
def problem6():
   for i in range(100):
       first_number=random.randint(1,6)
       second_number=random.randint(1,6)
       print(str(first_number)+'   '+str(second_number))

problem6()

"""
Heron's formula for computing the area of a triangle with sides a, b, and c is
as follows. Let s = .5(a + b + c) --- that is, 1/2 of the perimeter of the 
triangle. Then the area is the square root of s(s-a)(s-b)(s-c). You can compute
the square root of x by x**.5 (raise x to the 1/2 power). Use an input 
statement to get the length of the sides. Don't forget to convert this input 
to a real number using float(). Adjust your output to be just like what you
see below. Here is a run of my program:


"""
import math

def triangle_mathematics():
    a=float(input("Enter the length of first side"))
    b=float(input("Enter the length of second side"))
    c=float(input("Enter the length of third side"))
    perimeter=(a+b+c)/2
    partial_area=perimeter*(perimeter-a)*(perimeter-b)*(perimeter-c)
    area=math.sqrt(partial_area)
    print("Perimeter:"+str(perimeter))
    print("area:"+str(area))

triangle_mathematics()