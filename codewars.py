
def maskify(cc):
    val = list(cc)
    perem = 0
    countt = len(val)
    if countt > 4:
        while (perem < countt - 4):
            val[perem] = '#'
            perem+=1
    else:
        return ''.join(val)
    return ''.join(val)
print(maskify('1231424'))
print(maskify('dimasss'))
print(maskify(''))

"""
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
"""

