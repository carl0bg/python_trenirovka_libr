
def good_vs_evil2(good, evil):
   good = [int(i) for i in good.split()]
   evil = [int(i) for i in evil.split()]
   a, b, c, d, e, f = good
   a1, b1, c1, d1, e1, f1, g1 = evil
   dct_good = {'hobbits': 1*a, 'men': 2*b, 'elves': 3*c, 'dwarves': 3*d, 'eagles': 4*e, 'wizard': 10*f}
   dct_evil = {'orcs': 1*a1, 'men':2*b1, 'wargs':2*c1, 'goblin':2*d1, 'uruk hai':3*e1, 'trolls': 5*f1, 'wizards': 10*g1}
   if sum(dct_good.values())>sum(dct_evil.values()):
      return ('Battle Result: Good triumphs over Evil')
   elif sum(dct_good.values())<sum(dct_evil.values()):
      return ('Battle Result: Evil eradicates all trace of Good')
   else:
      return ("Battle Result: No victor on this battle field")
   



'''
def goodVsEvil(good, evil):

    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]
    
    good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
    evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])

    result = 'Battle Result: '
    
    if good < evil:
        return result +'Evil eradicates all trace of Good'
    elif good > evil:
        return result + 'Good triumphs over Evil'
    else:
        return result + 'No victor on this battle field'
'''


print(good_vs_evil2('1 1 1 1 1 1', '1 1 1 1 1 1 1'))