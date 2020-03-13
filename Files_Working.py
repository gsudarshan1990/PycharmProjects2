#Print the Working Directory

import os
print(os.getcwd())

def print_file():
    infile=open("E:\Python_Latest_Besant_Technologies\All_Text_Files\File1.txt")
    for line in infile:
        print(line)

    infile.close()

print_file()

def copy_file():
    infile=open("E:\Python_Latest_Besant_Technologies\All_Text_Files\File2.txt")
    outfile=open("E:\Python_Latest_Besant_Technologies\All_Text_Files\File2_Outfile.txt","w")

    for line in infile:
        outfile.write(line)

    infile.close()
    outfile.close()

copy_file()

def write_file(myname,myage,major):
    outfile=open("E:\Python_Latest_Besant_Technologies\All_Text_Files\File3_Outfile.txt","w")
    outfile.write("My name is "+myname+"\n")
    outfile.write("My age is "+myage+"\n")
    outfile.write("My major is "+major+"\n ")

write_file("Venky","27","Computer Science")
