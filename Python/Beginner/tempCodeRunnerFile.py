class Comp:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        return (self.a + other.a, self.b + other.b)

num1 = Comp(1, 2)
num2 = Comp(2, 4)

print(num1 + num2)