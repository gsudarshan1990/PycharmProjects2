#This describes about the files

#The most important function in the files is open

#files take two parameters 0. name of the file and 2. Mode of the file

#Below are certain mode types

#'r'-default value, to read the file and returns the error if file does not exits

# 'a' - append the existing file and create a new file if does not exits

# 'w' - writes to the existing file and create a new file if does not exist

# 'x' - creates a file and returns a error if file exists

# 't' - creates the file in the text mode

# 'b' - creates the file in the binary mode

#This is used to open the file
f = open("E:/Python_Latest_Besant_Technologies/read_example.txt")


#This is used to read the contents of the file
f = open("E:/Python_Latest_Besant_Technologies/read_example2.txt", 'r')
print(f.read())

#This is used to write the contents to the file
f = open("E:/Python_Latest_Besant_Technologies/write_example1.txt", 'a')
f.write('Data is writtern from the program')
f.close()

f = open("E:/Python_Latest_Besant_Technologies/write_example1.txt")
print(f.read())

