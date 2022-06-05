"""
Lambda
"""

list1 = [
  ['P1, 13'],
  ['P2, 6'],
  ['P3, 7'],
  ['P4, 50'],
  ['P5, 8'],
]

print(sorted(list1, key=lambda i: i[0], reverse=True))
print(list1)