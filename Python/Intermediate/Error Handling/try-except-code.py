a = input("Enter a number: ")
print(f"Multiplication table of {a} is: ")

try: 
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print("You've entered a string instead of a number!")

print("Blah blah blah")
print("End of Program")


# Handling specific errors 
try: 
    b = int(input("Enter a number: "))
    num = [4, 3]
    print(num[b])
except ValueError:
    print("Entered a non-integer!")
except IndexError:
    print("Invalid Index!")