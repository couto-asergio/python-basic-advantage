"""
Count - infinite Counter
"""
from itertools import count

count_1 = count()
list_1 = ['Luiz', 'João', 'Maria', 'José', 'Silva', 'Eduardo']

list_2 = zip(count_1, list_1)
print(list(list_2))
