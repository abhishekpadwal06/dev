class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

a1 = Puppy()
a1.eat()
a1.bark()
a1.weep()