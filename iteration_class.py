class ToUpperClass:
   def __init__(self, string_obj, position=0):
      self.string_obj = string_obj
      self.position = position
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.position >= len(self.string_obj):
         raise StopIteration() # raise - принудительное порождение исключения(ошибки)
      #position = self.position
      position = self.position
      self.position += 1
      return self.string_obj[position].upper()
   
low_python = 'python'
up_python = ToUpperClass(low_python)
for r in up_python:
   print(r)