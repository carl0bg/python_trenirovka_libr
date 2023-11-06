def disemvowel(strg):
   tren = ['a', 'o', 'e', 'i', 'u']
   ls = []
   for i in strg:
      if i in tren or i in [j.upper() for j in tren]:
         continue
      ls.append(i)
   return ''.join(ls)

def disemvowel1(strg):
   return ''.join([i for i in strg if i.lower() not in 'aoeiu'])


print(disemvowel1("What are you, a communist?"))