
'''
Write a function that removes the spaces from the string, then return the resultant string.
'''

def space(x):
   lst = [xx for xx in x if xx != ' ']
   return ''.join(lst)




print(space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))

'''
def no_space(x):
    return x.replace(' ' ,'')

def no_space(x):
    return "".join(x.split())

'''