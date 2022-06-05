"""
Create Modules
"""
import math

PI = math.pi

def double_list(list1):
  return [x*2 for x in list1]

def multiply(list1):
  r = 1
  for i in list1:
    r *= i
  return r

if __name__ == '__main__':
  list1 = [1, 2, 3, 4, 5]
  print(double_list(list1))
  print(multiply(list1))
  print(PI)

