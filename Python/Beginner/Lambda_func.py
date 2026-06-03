add = lambda a, b: a + b
print(add(2, 3))

square = lambda x: x * x
print(square(4))


# map(), filter(), reduce()
from functools import reduce

nums = [1, 2, 3, 4, 5]
res1 = list(map(lambda x: x * 2, nums))
print(res1)

res2 = list(filter(lambda x: x % 2 == 0, nums))
print(res2)

res3 = reduce(lambda x, y: x + y, nums)
print(res3)