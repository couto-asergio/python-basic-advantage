"""
Filter
"""
from data import people

def filters(person):
  if person['idade'] >= 18:
    return True
  else:
    return False

new_list = filter(filters, people)

for product in new_list:
  print(product)


