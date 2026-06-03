# Python doesn't traditionally support Method Overloading, but it can be achieved using default arguments!

class Maths:
    def add(self, a, b=0):
        return a + b
    
m = Maths()

print(m.add(5))
print(m.add(5, 6))