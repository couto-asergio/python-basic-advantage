"""
Zip - Union iterables
Zip_longest - Itertools
"""
import itertools

index = itertools.count()
city = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
state = ['SP', 'MG', 'BA']

city_state = zip(
  index,
  state,
  city,
)

for index, state, city in city_state:
  print( index, state, city)
