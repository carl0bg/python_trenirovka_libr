'''
a = [10, 20, 30, 40]
print(*a)
'''



def printPetNames(owner, **pets):
   print(f'Owner - {owner}')
   for i,j in pets.items():
      print(f'{i}: {j}')



printPetNames("Dima", dog = 'Pudel', fish= ['gold', 'ter', 'mis'], cat = 'Murs')