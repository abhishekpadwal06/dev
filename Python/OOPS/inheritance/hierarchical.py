class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def make_sound(self):
        print("Barking")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

a1 = Dog()
a2 = Cat()

a1.eat()
a1.make_sound()

a2.eat()
a2.make_sound()