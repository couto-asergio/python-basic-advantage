"""
Behavior of generators and Iterators
"""
# lists, tuples, str --> sequences --> iterable

name = 'Luiz Otávio'
iterator = iter(name)
generator = (letter for letter in name)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print('Look for')

for letter in generator:
  print(letter)

print('Look at the other one')

for letter in generator:
  print(letter)

print(next(generator))