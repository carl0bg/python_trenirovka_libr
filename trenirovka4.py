lst = [2, 3, 4, 5, 6]
print(list(filter(lambda x: x != 2, lst)))


def odd(num):
   if(num%2)==0:
      return True
   else:
      return False
   
out_filter = filter(odd, lst)
#print(list(out_filter))