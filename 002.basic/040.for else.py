"""
For Else
"""
name = ['john', 'Mary', 'Paul']

for value in name:
    if value.lower().startswith('j'):
        continue
    print(value)

