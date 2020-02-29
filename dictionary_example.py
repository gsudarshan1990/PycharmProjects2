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