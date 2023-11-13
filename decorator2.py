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
'''

from functools import wraps

def decorator(func):
   @wraps(func) #задача функции wraps – это копирование имени, документации, списка аргументов и т.д., для предотвращения перезаписи.
   def actual_func(*args, **kwargs):
      """Inner function within decorator, which does the actual work"""
      print(f'Before calling {func.__name__}')
      func(*args, **kwargs)
      print(f'After calling {func.__name__}')
   return actual_func

@decorator
def greet(name):
   """Says hello to somebody"""
   print(f'Hello, {name}!')

print(greet.__name__)
print(greet.__doc__)