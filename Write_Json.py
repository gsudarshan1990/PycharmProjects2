import json

book ={}

book['first_name']={
    'name':'tom',
    'address':'newyork',
    'phone':'12345355'
}

book['second_name']={
    'name':'Jim',
    'address':'california',
    'phone':'123432432'
}

s=json.dumps(book)

print(s)

with open("E:\Python_Latest_Besant_Technologies\JSON Files\writtern.json","w") as file_holder:
    file_holder.write(s)

