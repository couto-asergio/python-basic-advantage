"""
Map
"""

org_list = [1, 2, 3, 4, 5]


# define a function that returns the cube of `num`
def cube(num):
    return num**3


fin_list = list(map(cube, org_list))
print(fin_list)   # [1, 8, 27, 64, 125]


# Lambda Expressions
fin_list = list(map(lambda x: x**3, org_list))
print(fin_list)     # [1, 8, 27, 64, 125]


# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


