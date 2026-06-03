# example
dogs = ["Roscoe", "Roger", "Shooter", "Julie"]

# 'in' and 'not in' operator
print("Roger" in dogs)
print("Lewis" in dogs)

# Referenceing in lists
print(dogs[1])      # Indexing from 0 
print(dogs[-1])     # Indexing from -1
print(dogs[2:4])    # Excluding 4 and Including 2 (Therefore, only 2 and 3)

dogs.append("Togo")     # 1 item
dogs.extend(["Viola", "Sweetie"])       # Multiple items
dogs += ["Brody", "Rachel"]         # Just like extend
dogs += "Knight"        # Adds each letter separately

dogs.remove("K")
dogs.pop()

dogs.insert(2, "Chat")
dogs[1:1] = ["Bluey", "Bingo", "Shishimaru"]

# dogs.sort()     # Sorts uppercase first, then lowercase
 
# dogs.sort(key=str.lower)    # To solve this problem, use -

# But what both these sorts do it, they make changes to the original list! In order to have original list unchanged and to have the list sorted and printed at the same time - 
print(sorted(dogs, key=str.lower))
print(dogs)



# List compression
numbers = [1, 2, 3, 4, 5]       
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2) 