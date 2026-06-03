# Simple class example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

d1 = Dog("Viola", 8)

print(d1.name)
print(d1.age)
d1.bark()





# Class with inheritance
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        return "walking..."
    
class Dog(Animal):              # Child (Dog) is inhereting from parent (Animal)
    def bark(self):
        print(f"{self.name} is {self.age} years old and she is {self.walk()}")

d1 = Dog("Viola", 6)
d1.bark()