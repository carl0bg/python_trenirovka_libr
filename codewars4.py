'''
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
'''


def duplicate_count(text):
   text = list(text.lower())
   text2 = text[:]
   perem = 0
   replay = 0
   for t in text:
      if replay>1:
         perem +=1
      replay =0
      for x in text2:
         if t == x:
            replay += 1
            text2[text2.index(x)] = '.'
   return perem

'''
def duplicate_count(text):
   if not text:
      return 0
   repite = 0
   dd = []
   d = [i for i in text.lower()]
   for i,k in enumerate(d, start=0):
      x = d.count(k)
      if x >=2 and k not in dd:
         repite += 1
         dd.append(k)
   return repite

'''
'''
def duplicate_count(text):
   return sum(1 for i in set(text.lower()) if txt.count(i)>1) if (txt := text.lower()) else 0
'''

print(duplicate_count("NfAJA3XQxYTt"))