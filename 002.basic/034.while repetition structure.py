"""
While - Repetition structure
"""

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Finish')

x = 0  # column
y = 0  # line

while x < 5:
    x += 1

print('Finish')

while True:
    print()
    num_1 = input('Type a number: ')
    num_2 = input('Type another number: ')
    operator = input('Type a operator: ')

    if operator == '+':
        print(num_1 + num_2)
    elif operator == "-":
        print(num_1 - num_2)


