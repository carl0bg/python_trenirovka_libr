'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer.
 If it is zero, it just returns "now".
  Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
'''


def format_duration(seconds):
   min = hh = days = years = 0
   while seconds >= 60:
      min+=1
      seconds-= 60
      if min >= 60:
         hh+=1
         min -= 60
      if hh >= 24:
         days += 1
         hh -= 24
      if days >= 365:
         days -= 365
         years += 1
   ls = []
   if years != 0:
      if years == 1:
         ls.append(f'{years} year')
      else:
         ls.append(f'{years} years')
   if days != 0:
      if days == 1:
         ls.append(f'{days} day')
      else:
         ls.append(f'{days} days')
   if hh != 0:
      if hh == 1:
         ls.append(f'{hh} hour')
      else:
         ls.append(f'{hh} hours')
   if min != 0:
      if min == 1:
         ls.append(f'{min} minute')
      else:
         ls.append(f'{min} minutes')
   if seconds != 0:
      if seconds == 1:
         ls.append(f'{seconds} second')
      else:
         ls.append(f'{seconds} seconds')
   if len(ls) == 0:
      return 'now'
   if len(ls) == 1:
      return ls[0]
   if len(ls) == 2:
      return f'{ls[0]} and {ls[1]}'
   prin = []
   if len(ls) > 2:
      for i in ls:
         if ls.index(i) == len(ls) - 2:
            prin.append(f'{i} and {ls[ls.index(i) + 1]}')
            return ''.join(prin)
         else:
            prin.append(f'{i}, ')
 
print(format_duration(424242455))


'''
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
'''