#Using the Python Copy function

thisdict={
    "brand":"Ford",
    "model":"Ecosport",
    "year":1964
}

newdict=thisdict.copy()
print(newdict)

thisdict={
    "brand":"Ford",
    "model":"Ecosport",
    "year":1964

}

seconddict=dict(thisdict)
print(seconddict)


#Nested Dictionary

myfamily={
    "child1":
        {
            "name":"emil",
            "year":2004
        },
    "child2":{
       "name":"Tobias",
        "year":2007
    },

    "child3":
        {
            "name":"Linus",
            "year":2011
        }
}

print(myfamily)

#Nested Dictionary part 2

child1={
    "name":"Emil",
    "year":2004
}

child2={
    "name":"Tobinas",
    "year":2007
}

child3={
    "name":"Linus",
    "year":2011
}

myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print(myfamily)