

class A:
   x = 5
   y= 2

   def __init__(self, a:float):
      self.a = a

   # def add(self, a:int, b:int):
   #    return a+b
 
   @classmethod #помогает использовать какую то функцию относительно нашего класса
   def sub(cls):
      return cls(13) #выходит экземпляр класса
      #return cls.x - cls.y


print(A.sub().__dict__)


# instance = A()
# A.add =classmethod(A.add)

