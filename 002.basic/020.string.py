"""
Variables
Start with letters, may contain numbers, to separate _,
lowercase letters
"""
name = 'Many Money'     # String
age = 32                # int
height = 1.80           # float
e_age = age > 18        # bool
date_1 = True
current_date = 2021
weight = 80
imc = weight / (height ** 2)

print(name, 'has', age, 'years old and your imc is', imc)
print(f'{name} has {age} years old and your imc is {imc:.2f}')
