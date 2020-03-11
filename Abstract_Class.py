#Example of the Abstract Method

from abc import ABC,abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can move and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can move and run and use four legs")

class Lion(Animal):
    def move(self):
        print("I can move lonely")

R=Human()
R.move()

R=Snake()
R.move()

R=Dog()
R.move()

R=Lion()
R.move()