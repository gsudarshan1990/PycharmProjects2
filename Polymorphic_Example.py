#In built Polymorphic Function

print(len("geeks"))

print(len([10,20,30]))


#Example of Polymorphic
class India():
    def capital(self):
        print('New Delhi is the Capital of India')

    def language(self):
        print('India has multi languages')

    def type(self):
        print("India is a developing country")


class USA():
    def capital(self):
        print("Washington D.C is the Capital of America")

    def language(self):
        print('English is the language of the North America')

    def type(self):
        print('America is a developed Country')

obj_india=India()
obj_usa=USA()

for country in (obj_india,obj_usa):
    country.capital()
    country.language()
    country.type()