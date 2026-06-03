# Simple class and objects example

class Dog: 
    def __init__(self, name, breed, age, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def walk(self, name):
        print(f"{name} takes me for a walk!")
    
    def bark(self):
        print("Woof woof!")

class Owner:
    def __init__(self, name):
        self.name = name

owner1 = Owner("Abhishek")
dog1 = Dog("Roscoe", "German", 2, owner1)

owner2 = Owner("Aditya")
dog2 = Dog("Viola", "Huskey", 2, owner2)

print(dog1.name, dog1.breed, dog1.age, dog1.owner.name)
dog1.walk(dog1.owner.name)

print("\n")

print(dog2.name, dog2.breed, dog2.age, dog2.owner.name)
dog2.walk(dog2.owner.name)