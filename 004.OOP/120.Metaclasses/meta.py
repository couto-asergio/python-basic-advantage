"""
 In Python all is a object: Include class
    MetaClass are the classes that create classes.
    Type is a MetaClass.
"""


class Father:
    name = 'Test'


A = type('A', (Father, ), {'attr': 'Hi World'})

a = A()
print(a.name)
