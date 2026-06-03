# Simple
print(1 + 2)
print("Geeks " + "for " + "Geeks")
print(3 * 5)
print("GFG " * 4)





# Operator overloading on User-defined functions - 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):  # overloading '>' operator
        return self.age > other.age

    def __add__(self, other):   # overloading '+' operator
        return self.age + other.age

Viola = Dog('Viola', 8)
Roger = Dog('Roger', 7)

print(Roger + Viola)



# Overloading + operator for complex numbers - 
class Comp:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        return (self.a + other.a, self.b + other.b)

num1 = Comp(1, 2)
num2 = Comp(2, 4)

print(num1 + num2)