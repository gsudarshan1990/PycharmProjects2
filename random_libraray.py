import random

#Usage of the random libraries
print(random.random())
print(random.random())
print(random.random())
print(random.random())

print(random.randint(3,8))
print(random.randint(3,8))
print(random.randint(3,8))
print(random.randint(3,8))

#Declaring the four lists and usage of the libraries


verbs=["goes","cooks","shoots","faints","chews","screams"]
nouns=["bear","lion","mother","baby","sister","car","bicycle","books"]
adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"]

def sentence():
    verb=random.choice(verbs)
    noun=random.choice(nouns)
    adverb=random.choice(adverbs)
    article=random.choice(articles)

    our_sentence=article+" "+noun+"  "+verb+"   "+adverb
    our_sentence=our_sentence.capitalize()

    print(our_sentence)

sentence()
