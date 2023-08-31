'''
You are going to be given an array of integers.
Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
If there is no index that would make this happen, return -1
'''

def find_even_index(arr):
    perem = sum(arr)/2
    if (len(arr) == 0):
        return 0
    perem2=0
    p = 0
    while p!=len(arr):
        if perem2+(arr[p])/2 == perem:
            return p
        perem2 += arr[p]
        p+=1
    return (-1)

'''
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
'''
print(find_even_index([1,2,3,4,3,2,1]))


    