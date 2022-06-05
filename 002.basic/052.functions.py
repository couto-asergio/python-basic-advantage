"""
Function - def
"""
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

def salutation(msg='Hi', name='user'):
    name = name.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {name}'

var1 = salutation()
print(var1)

def func(*args, **kwargs):
    print(args)
    age = kwargs.get('age')
    if age is not None:
        print(age)

func(*list1, *list2, name='Luiz', lastname='Miranda', age=30)

var10 = 'value'

def func():
    other_var = 'Richard'
    return other_var

def func2(arg):
    print(arg)

var = func()
func2(var)