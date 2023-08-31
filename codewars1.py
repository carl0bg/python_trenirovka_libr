import string

'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
'''

def is_isogram(word): 
    word = word.lower()
    for w in word:
        if word.count(w)>1:
            return False
    return True

print(is_isogram('Dermatoglyphics'))
print(is_isogram('moose'))

'''
def is_isogram(string):
    return len(string) == len(set(string.lower()))
'''