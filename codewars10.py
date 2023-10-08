
def reverse_words(text):
   res = [i[::-1] for i in text.split(' ')]
   return ' '.join(res)


def reverse_words2(str):
    return ' '.join(s[::-1] for s in str.split(' '))

print(reverse_words("This  is  an  example!"))
