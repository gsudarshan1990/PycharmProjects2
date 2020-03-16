import json

#From Json Object to the Python Dictionary Object
json_data='{"a":1,"b":2,"c":3,"d":4,"e":5}'

parsed_json=json.loads(json_data)
print(parsed_json)
print(parsed_json['a'])


#From the Python Dictionary object to the Json object

json_data_from_python=json.dumps(parsed_json,indent=4)
print(json_data_from_python)

#From Json to Python and priting in the form of the dictionary

for key,value in parsed_json.items():
    print(key+"  ",value)


#Loading from the json file to python

with open("E:\Python_Latest_Besant_Technologies\JSON Files\sample.json","r") as file_header:
    new_json=json.load(file_header)

print(new_json)





