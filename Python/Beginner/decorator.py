def my_decorator(funct):
    def pre_func():
        print("Welcome to F1 Paddock Club!")
        name = funct()
        print(f"How can we help you, {name}?")
    return pre_func

@my_decorator
def hello():
    name = input("Please enter your name: ")
    print(f"Hello {name}")
    return name

hello()