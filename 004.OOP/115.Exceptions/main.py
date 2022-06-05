"""
    Exceptions
"""


class Error(Exception):
    pass


def test():
    raise Error('Wrong')


try:
    test()
except Error as error:
    print(f'Error: {error}')
