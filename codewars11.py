'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.


'''


def make_readable(seconds):
   min = hh = 0
   while seconds >= 60:
      min+=1
      seconds-= 60
      if min >= 60:
         hh+=1
         min -= 60
   if hh<10:
      hh = str(f'0{hh}')
   if min<10:
      min = str(f'0{min}')
   if seconds<10:
      seconds = str(f'0{seconds}')

   return f'{hh}:{min}:{seconds}'

def make_readable(s):  
    return f'{s // 3600:02}:{s // 60 % 60:02}:{s % 60:02}'


def make_readable2(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

print(make_readable2(60))