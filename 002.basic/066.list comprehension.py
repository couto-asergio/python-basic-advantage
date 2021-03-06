h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)


h_letters = [letter for letter in 'human']
print(h_letters)


# List Comprehensions vs Lambda functions
letters = list(map(lambda x: x, 'human'))
print(letters)


# Conditionals in List Comprehension
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)


# Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)


# if...else With List Comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)


# Nested Loops in List Comprehension
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


# Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)

