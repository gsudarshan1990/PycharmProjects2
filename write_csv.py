import csv

List1=[["Name","Phone","City"],
       ["sonu","123423434","Hyderabad"],
       ["deepu","13434243","Hyderabad"],
       ["Manjunath","14243434343","bengaluru"],
       ["Sethu","34342","Chennai"]
       ]


def write_to_csv(filename):
    with open(filename,"w") as file_header:
        for line in List1:
            csv.writer(file_header).writerow(line)


write_to_csv("E:\Python_Latest_Besant_Technologies\CSV_File\writtencsv.csv")