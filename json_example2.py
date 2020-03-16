import json

json_object='{"name":"Shashank","age":29,"job":"IT Engineer"}'

parsed_json_dict=json.loads(json_object)

print(parsed_json_dict)

for key, value in parsed_json_dict.items():
    print(key+"   "+str(value))



with open("E:\Python_Latest_Besant_Technologies\JSON Files\secondjson.json","r") as file_header:
    new_parsed_json_dict=json.load(file_header)

for key,value in new_parsed_json_dict.items():
    print(key+"   ",value)