"""
Docorator
"""

from time import time
from time import sleep

def velocity( function):
  def internal(*args, **kwargs):
    start_time = time()
    result = function(*args, **kwargs)
    end_time = time()
    t = (end_time - start_time) * 1000
    print(f'\nFunction {function.__name__}'
          f'took {t:.2f}ms to execute.')
    return t
  return internal
