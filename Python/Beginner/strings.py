"Lewis"
'Lewis'

name = "Lewis" + " Hamilton"
print(name)

name2 = name + " 44"
print(name2)

name += " 44"
print(name)

name = ("""
Lewis
Hamilton
""")
print(name)


# String methods

# 1. upper()
print('Lewis'.upper())  # LEWIS

# 2. lower()
print('lEWis'.lower())  # lewis

# 3. title()
print('lewis'.title())  # Lewis (Capitalized first letter)

# 4. islower()
print('Lewis'.islower())    # False

# 4. isupper()
print('LEWIS'.iupper())    # True

# 5. isalpha() - to check if a string contains only characters and is not empty
# 6. isalnum() - to check if a string contains characters or digits and is not empty
# 7. isdecimal() - to check if a string contains digits and is not empty
# 8. startswith() - to check if a string starts with a specific substring
# 9. endswith() - to check if a string ends with a specific substring
# 10. replace() - to replace a part of a string
# 11. split() - to split a string on a specific character separator
# 12. strip() - to trim the whitespaces from a string
# 13. join() - to append new letters to a string
# 14. find() - to find the position of a substring


name = 'Lewis'
print(len(name))            # 5

name4 = "Hamilton"
print('mil' in name4)       # True

name5 = "Hamilton"
print('mill' in name5)      # False

name6 = "Hami\"lton"
print(name6)        # Escaping - Used to use a "" in a string

name6 = 'Hami"lton'
print(name6)        # No need of escaping here as " is in two single quotes

name7 = "Ham\nilton"
print(name7)        # New line character

name8 = "Ham\\ilton"
print(name8)

name9 = "Lewis"
print(name9[1])         # Indexing from front starts from 0

name9 = "Lewis"
print(name9[-1])        # Indexing from back starts from -1


# Slicing
name10 = "Lewis Hamilton"
print(name10[1:7])          # Including 1 and Excluding 7       Therefore -> 'ewis H'
print(name10[:15])
print(name10[0:])