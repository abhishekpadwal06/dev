# Simple while loop
count = 0
while count < 10:
    count += 1
    print(count)





# For loop 
items = [1, 2, 3, 4, 5]
for i in items:
    print(i)





# For loop in range
for i in range(1, 15):
    print(i)





# For loop using enumerate
items = [1, 2, 3, 4, 5]
names = ["Chandler", "Joey", "Ross", "Rachel", "Phoebe", "Monica"]
for j in enumerate(names):      # We can use names or items (Works for both)
    print(j)





# Continue Statement
for i in range(1, 5):
    if i == 2:
        continue
    print(i)





# Break Statement
for i in range(1, 5):
    if i == 3:
        break
    print(i)