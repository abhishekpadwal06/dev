# Simple example
def greeting():
    def printing(name):
        print(f"Hello {name}, Welcome to F1 community!")
        
    name = input("Please enter your name: ")
    printing(name)

greeting()



# Interesting example
def count():
    count = 0

    def incr():
        nonlocal count          # (USED SPECIALLY FOR CLOSURES) used to access a variable in inner function which is defined in outer function
        count = count + 1
        print(count)
    
    incr()

count()