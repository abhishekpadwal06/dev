set1 = {1, 2, 3, 5, 5, 6, 7}
set2 = {1, 2, 3, 6, 7, 7}

intersect = set1 & set2     # intersection set
print(intersect)

union = set1 | set2         # union set
print(union)

diff = set1 - set2          # difference set (Not present in 2nd set, but, present in 1st set)
print(diff)

superset = set1 > set2        # superset
print(superset)

subset = set1 < set2          # subset
print(subset)