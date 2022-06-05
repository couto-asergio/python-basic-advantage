"""
 Logics Operators
 and, or, not, in and not in
"""
user = input('User name:')
passw = input('User password:')

user_bd = 'Wilson'
passw_bd = '123456'

if user_bd == user and passw_bd == passw:
    print('You is logged')
else:
    print('User or passw invalid')
