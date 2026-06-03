# To understand static methods, consider the following example: 
class Player: 
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def greet():
        print("Hello!")

p1 = Player("Abhishek", "Football")
p1.greet()

# This will throw an error because there's no 'self' in the greet(). But if you see carefully, 'self' doesn't make sense in this func.
# Therefore, what we can do is, we can create a 'static method'
# Static methods: methods that don't use self parameter (work at class level)
# Example - 

class Player: 
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    @staticmethod       # This is a decorator which is used to convert a method into static method
    def greet():
        print("Hello!")

p1 = Player("Abhishek", "Football")
p1.greet()