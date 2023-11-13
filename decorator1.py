'''
def decorator(call):
   def wrapper(*args, **kwargs):
      r = call(*args, **kwargs)
      return r
   return wrapper


def call(a:int) -> str:
   return str(a)

decorated_call = decorator(call)

assert decorated_call(1) == '1'
'''
'''
from functools import wraps

def decorator(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
      return func(*args, **kwargs)
   return wrapper
'''

def decorator(func):
   def actual_func(*args, **kwargs):
      print(f'Before calling {func.__name__}')
      func(*args, **kwargs)
      print(f'After calling {func.__name__}')

   return actual_func


@decorator
def greet(name):
   print(f'Hello, {name}!')

greet('Martin')
