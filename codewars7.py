'''
Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
 The input will be a non-negative integer.
 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
'''


def digital_root(n):
   lst = [int(i) for i in str(n)]
   while len(lst)>1:
      sm = sum(lst)
      lst = [int(i) for i in str(sm)]
   return lst[0]



'''
def digital_root3(n):
    return n if n < 10 else digital_root3(sum(map(int,str(n))))

def digital_root(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n
'''

print(digital_root(493193))