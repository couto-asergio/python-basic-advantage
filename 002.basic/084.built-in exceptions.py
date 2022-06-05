"""
Built-in Exceptions
https://docs.python.org/3/library/exceptions.html
"""
def divide(n1, n2):
  if n2 == 0:
    raise ValueError("n2 don't can be 0.")
  return n1 / n2

try:
  print(divide(n1=2, n2=0))
except ValueError as error:
  print('Division by zero.')
  print('Log:', error)
