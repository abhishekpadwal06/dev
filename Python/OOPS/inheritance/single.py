class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

a1 = Dog()
a1.eat()
a1.bark()