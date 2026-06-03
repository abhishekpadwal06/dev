age = 20
# Arithmetic Operators

1 + 1
1 + -0  # 0
2 - 1
2 * 2
4 / 2
4 % 3       # Remainder -> 4 % 3 = 1
4 ** 2      # Raised to the power -> 4 ** 2 = 16
5 // 2      # Floor division -> 5 / 2 = 2.5     BUT     5 // 2 = 2 




# Comparison Operators
==, <, >, >=, <=, !=




# Boolean Operators
done = True
not_done = False

# Question 
book_1_read = True
book_2_read = False
print(all([book_1_read, book_2_read]))

book_1_read = True
book_2_read = False
print(any([book_1_read, book_2_read]))



# Logical Operators
not, and, or

# Questions -     
print(0 or 1)               # 1
print(False or 'hey')       # 'hey'
print('hi' or 'hey')        # 'hi'
print([] or False)          # 'False'
print(False or [])          # '[]'


print(0 and 1)              # 0
print(1 and 0)              # 0
print(False and 'hey')      # False
print('hi' and 'hey')       # 'hey'
print([] and False)         # []
print(False and [])         # False



# Bitwise Operators 
& - Binary AND 
| - Binary OR
^ - Binary XOR
~ - Binary NOT
<< - Left Shift operation
>> - Right Shift operation



# Identity operator - is
# Membership operator - in



# Ternary operator 
# Shortcut / Short form of if else

# Old school if-else
def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# Shortcut (Ternary Operator)
def is_adult2(age):
    return True if age > 18 else False



