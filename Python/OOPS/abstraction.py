from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

a1 = Dog()
a2 = Cat()

a1.make_sound()
a2.make_sound()