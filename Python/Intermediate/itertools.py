# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

# Product
from itertools import product
a = [1, 2, 3]
b =  [4, 5, 6]
prod1 = list(product(a, b))
print(prod1)             # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

c = [1, 2]
d = 'a'
prod2 = list(product(c, d, repeat = 2))     # [(1, 'a', 1, 'a'), (1, 'a', 2, 'a'), (2, 'a', 1, 'a'), (2, 'a', 2, 'a')]
print(prod2)




# Permutations
from itertools import permutations

e = [1, 2, 3]
res = list(permutations(e, 2))  
print(res)                      # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

res = list(permutations(e))     
print(res)                      # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]




# Combinations
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))              # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb = combinations_with_replacement(a, 2)
print(list(comb))              # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]





# Accumulate function
from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)            # [1, 2, 3, 4]
print(list(acc))    # [1, 3, 6, 10]         # Addition

import operator
acc = accumulate(a, func=operator.mul)      # Multiplication
print(list(acc))      # [1, 2, 6, 24]

b = [1, 2, 5, 3, 4]
acc = accumulate(b, func=max)      # Returns maximum element from the list
print(b)              # [1, 2, 5, 3, 4]
print(list(acc))      # [1, 2, 5, 5, 5]  Compares current element with previous max element and returns the max of the two elements





# groupby
from itertools import groupby
# def smaller_than_3(x):
#     return x < 3
# a = [1, 2, 3, 4]
# group_obj = groupby(a, key=smaller_than_3)
# for key, val in group_obj:
#     print(key, list(val))           # True [1, 2]       False[3, 4]


# # same using lambda function
# group_obj = groupby(a, key = lambda y: y < 3)
# for(key, val) in group_obj:
#     print(key, list(val))


# Dictionaries
persons = [ {'name': 'Lewis', 'age': 41}, {'name': 'Max', 'age': 28}, 
            {'name': 'Charles', 'age': 28}, {'name': 'Fernando', 'age': 44}]

group_obj = groupby(persons, key=lambda x : x['age'])
for(key, val) in group_obj:
    print(key, list(val))       # 41 [{'name': 'Lewis', 'age': 41}]
                                # 28 [{'name': 'Max', 'age': 28}, {'name': 'Charles', 'age': 28}]
                                # 44 [{'name': 'Fernando', 'age': 44}]




# Count, Cycle, Repeat

# Count
from itertools import count, cycle, repeat
for i  in count(10):        # Infinite loop that starts from 10
    print(i)
    if i == 15:
        break



# Cycle
a = [1, 2, 3]
for i in cycle(a):          # Infinite loop of 1, 2, 3
    print(i)



# Repeat
for i in repeat(1, 4):         # Repeat '1', 4 times
    print(i)