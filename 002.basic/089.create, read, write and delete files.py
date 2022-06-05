"""
Create, Read, Write and Delete files.
https://docs.python.org/3/library/functions.html#open
"""
import json

try:
  file = open('abc.txt', 'w+')
  file.write('Line')
  file.seek(0)
  print(file.read())
finally:
  file.close()


with open('abc.json', 'r') as file:
  d1_json = file.read()
  d1_json = json.loads(d1_json)

for k, v in d1_json.items():
  print(k)
  for k1, v1 in v.items():
    print(k1, v1)
