import csv


#Printing from the file
def read_from_csv(filename):
   with open(filename) as file_header:
       for line in csv.reader(file_header):
           print(line)


read_from_csv("E:\Python_Latest_Besant_Technologies\CSV_File\Secondcsv.csv")


#Printing in the form of lists

def seocond_read_from_csv(filename):
   data=list()
   with open(filename) as file_header:
       for line in csv.reader(file_header):
           data.append(line)
   print(data)





seocond_read_from_csv("E:\Python_Latest_Besant_Technologies\CSV_File\Secondcsv.csv")
