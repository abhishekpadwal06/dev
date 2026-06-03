# Syntax: 
# try: 
    # Block of code which could generate exception
# except:
     # Solution to generated exception
# finally: 
     # Block of code which is going to execute in any situation

# Example
try:
    lst = [1, 2, 3, 4, 5]
    a = int(input("Enter a number: "))
    print(lst[a])
except: 
    print("Error occurred!")
finally: 
    print("I am always executed!")

# Now what's the use of finally I could've simply done this! --> 


try:
    lst = [1, 2, 3, 4, 5]
    a = int(input("Enter a number: "))
    print(lst[a])
except: 
    print("Error occurred!")

print("I am always executed!")

# This will also print ("I am always executed") everytime irrespective of whether error occurred or not!
# Reason: For this, let us consider a function in which we are returning something. In that case, this above example won't print ("I am always executed"). Example --> 


def func1():
    try:
        lst = [1, 2, 3, 4, 5]
        a = int(input("Enter a number: "))
        print(lst[a])
        return 1
    except: 
        print("Error occurred!")
        return 0

    print("I am always executed!")

x = func1()
print(x)


# Now in this eg, in both the cases, you won't be able to see ("I am always executed"). That's because the function returns value and the control gets transferred before it comes to the print("I am always executed!") line of the function
# So, in order to overcome this and in order to print that line always, we have to use 'finally' block!


def func2():
    try:
        lst = [1, 2, 3, 4, 5]
        a = int(input("Enter a number: "))
        print(lst[a])
        return 1
    except: 
        print("Error occurred!")
        return 0
    finally:
        print("I am always executed!")

y = func2()
print(y)