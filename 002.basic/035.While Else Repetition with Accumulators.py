"""
While/Else
"""

counter = 1
accumulators = 1

while counter <= 10:
    print(counter, accumulators)

    accumulators = accumulators + counter
    counter += 1
else:
    print('I arrived the else!')
print('out of else')
