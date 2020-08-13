#what is a frozen set? can we change the values of the frozen set

#frozen set takes the iterator and is immutable hence we cannot change the value


vowels = ('a','e','i','o','u')

f = frozenset(vowels)
print(f)


dictionary1  = {'name':'sonu','age':28}

f2 = frozenset(dictionary1)
print(f2)