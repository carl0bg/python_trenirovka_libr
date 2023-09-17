
'''
Нахождение периметра, по принципу Фибоначчи
'''

def perimeter(n):
   lst = [1, 1]
   perem = 0
   index = 1
   while True:
      if len(lst) == n+1:
         perim = 4*sum(lst)
         return perim
      perem = lst[index-1] + lst[index]
      lst.append(perem)
      index += 1

print(perimeter(20))

'''
def perimeter(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1
    return 4 * (b - 1)
'''