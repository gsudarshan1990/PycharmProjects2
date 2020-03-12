#this is the example of dictionary

thisdict={
    "Name":"sheldon",
     "Age":10,
    "Country":"US"
}

#Print the dictionary
print(thisdict)

#Accessing the Specific key
thisdict={
    "Name":"sheldon",
    "Age":10,
    "Country":"US"
}

x=thisdict["Name"]
print(x)

#Change value in dictionary
thisdict["Country"]="UK"
print(thisdict)

#Iterating the dictionarykeys:
for x in thisdict:
    print(x)

#Print all the key values
for x in thisdict:
    print(thisdict[x])

#print the values
print("===========================")
for x in thisdict.values():
    print(x)

#Printing the key values in the form of tuple
for x,y in thisdict.items():
    print(x,y)


#Checking whether the key exists
thisdict={"Name":"Sheldon","Age":10,"Country":"UK"}
if 'Age' in thisdict:
    print("Age exits")

#Adding the new value to the existing dictionary
thisdict={"Name":"Sheldon","Age":10,"Country":"UK"}
thisdict["nickname"]="Shelly"
print(thisdict)


#Dictionary
d={"Johny":"5 years old","Sally":"7 years old","Eva":"10 years old","peggy":"7 years old"}
print(d)

print(d["Sally"])
print(d["Eva"])
print(d.items())
print(d.keys())
print(d.values())


#Print Key and Value Separately
for key,value in d.items():
    print(key+"------>"+value)


#Printing in the form of tuples
for item in d.items():
    print(item)

#Pring in the form of values from d.items()

for item in d.items():
    print(item[0]+'------>'+item[1])

for key in d.keys():
    print(key+'---->'+d[key])

d['Ted']='5 years old'

ascars={"Ford":"Mustang","Mazda":"Miata","Scion":"FR-S","Subaru":"BRZ","Dodge":"Challenger","Nissan":"3702","chevy":"Camaro",
        "Hyundai":"Genesis Coupe","Mini-Cooper":"Roadster"}

print(ascars)
print(ascars['Nissan'])
print(ascars['chevy'])
print(ascars['Mini-Cooper'])
ascars['Mini-Cooper']='coupe'

for value in ascars.values():
    print(value)

for key in ascars.keys():
    print(key)
