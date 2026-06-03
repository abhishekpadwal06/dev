class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")

a1 = Dog() ; a2 = Cat()     # ; - used when we want to write two different lines of code onto one single line

a1.eat()
a2.eat()



# Instead of this, we can do this - 

class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")

for animal in [Dog(), Cat()]:
    animal.eat()