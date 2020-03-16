import csv

def read_from_csv(filename):
    with open(filename) as file_header:
        for line in csv.reader(file_header):
            print(line)

read_from_csv("E:\Python_Latest_Besant_Technologies\CSV_File\Sample.csv")