"""
Combinations  - Order doesn't matter
Permutations  - Order does matter.
Product       - Order does matter and repeats unique values.
Itertools
"""

from itertools import combinations, permutations, product

people = list_1 = ['Luiz', 'João', 'Maria', 'José', 'Silva', 'Eduardo']

for group in combinations(people, 3):
  print(group)