'''
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
'''

def likes(names):
   if (len(names)==0):
      return 'no one likes this'
   elif (len(names)==1):
      return '{0} likes this'.format(*names)
   elif (len(names) == 2):
      return '{0} and {1} like this'.format(*names)
   elif (len(names == 3)):
      return '{0}, {1} and {2} like this'.format(*names)
   else:
      return f'{names[0]}, {names[1]}, and {len(names)-2} others like this'

'''
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
'''