#This  is used to write the contents to the file


try:
    f = open("E:/Python_Latest_Besant_Technologies/write_example4.txt",'w')
    f.write('hello everyone !')
except IOError:
    print('can\'t find the file or read')
else:
    print('Written the contents to the file')

try:
    f = open("E:/Python_Latest_Besant_Technologies/write_example4.txt",'r')
    print(f.read())
finally:
    f.close()
    