"""
try, Except - Handling Exception
"""

try:
  a = 0
  try:
    a = 1/0
  except:
    print('Error')
except NameError as err:
    print('Developer error. Talk to him.')
except(IndexError, KeyError) as err:
  print('Index error or key.')
except Exception as err:
  print('Unexpected error')
else:
  pass
finally:
  a = ''

print(a)

