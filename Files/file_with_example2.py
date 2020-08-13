#This is used to explain about the with statement

#Below is the first example without using the with statement
f = open("E:/Python_Latest_Besant_Technologies/with_example0.txt",'w')
f.write('Hello everyone!')
f.close()

#Below is the second example without using the with statement
f = open("E:/Python_Latest_Besant_Technologies/with_example1.txt",'w')
try:
    f.write('Good morning everyone')
finally:
    f.close()

#Below is opening the file with the help of the with statement

with open("E:/Python_Latest_Besant_Technologies/with_example3.txt", 'w') as f:
    f.write("hello every one using the with statement")

