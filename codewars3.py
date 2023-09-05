
def array_diff(a, b):
    for x in b:
       while a:
         if x in a:
            a.remove(x)
         else:
            break
    return a



print(array_diff([1, 2, 2], [2])) # = [1]

'''
def array_diff(a, b):
    return [x for x in a if x not in b]
'''

'''
def array_diff(a, b):
    return filter(lambda i: i not in b, a)
'''