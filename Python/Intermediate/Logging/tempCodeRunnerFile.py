from itertools import count, cycle, repeat
for i  in count(10):        # Infinite loop that starts from 10
    print(i)
    if i == 15:
        break



# Cycle
a = [1, 2, 3]
for i in cycle(a, 3):          # Infinite loop of 1, 2, 3
    print(i)



# Repeat
for i in repeat(1, 4):         # Repeat '1', 4 times
    print(i)