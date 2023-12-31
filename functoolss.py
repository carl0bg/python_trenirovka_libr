# from functools import total_ordering #как бы должен за нас реализовывать eq, lt, le, gt или ge

# @total_ordering
# class B:
#    def __init__(self, value):
#       self.value = value

#    def __lt__(self, other):  #<
#       return self.value < other.value
   
#    def __eq__(self, other):
#       return self.value == other.value
   
# print(B(10)<B(20))
# print(B(300)==B(300))

from functools import singledispatchmethod
from datetime import date, time

class Formatter:
   @singledispatchmethod
   def format(self, arg):
      raise NotImplementedError(f"Cannot format value of type {type(arg)}")

   @format.register
   def _(self, arg: date):
      return f"{arg.day}-{arg.month}-{arg.year}"
   
   @format.register
   def _(self, arg: time):
      return f"{arg.hour}:{arg.minute}:{arg.second}"
   
f = Formatter()
print(f.format(date(2021, 5, 26)))
print(f.format(time(19, 22, 15)))


