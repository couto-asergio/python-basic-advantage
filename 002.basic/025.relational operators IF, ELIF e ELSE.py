"""
Conditions IF, ELIF e ELSE
== > >= < <= !=
== equality > bigger then
>= bigger then or equal a
< less than
<= less than or equal a
!= different
"""

num_1 = 2   # int
num_2 = 2   # int

expression = (num_1 > num_2)

print(expression)

name = input("What's is your name?")
age = input("What's your age?")

age_limit = 18

if age >= age_limit:
    print(f'{name} you can take the loan')
else:
    print(f"{name} you can't borrow")
