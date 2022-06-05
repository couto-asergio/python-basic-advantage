"""
Reducer
"""
from data import product, people, list_1
from functools import reduce

age_sum = reduce(lambda ac, p: ac + p['age'], people, 0)
print(age_sum / len(people))
