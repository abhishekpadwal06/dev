class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")
    
class Cat(Animal):
    def sound(self):
        print("Meow!")

d = Dog()
c = Cat()

d.sound()
c.sound()