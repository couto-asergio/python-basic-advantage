"""
Generators, Iterators and Iterables
"""

import sys
import time

def generator():
  for n in range(100):
    yield time.sleep(0.1)
    time.sleep(0.1)

g = generator()

for v in g:
  print(v)

lists = [x for x in range(1000000)]
print(sys.getsizeof(lists))

l1 = [x for x in range(1000000)]
l2 = (x for x in range(1000000))

for v in l2:
  print(v)


