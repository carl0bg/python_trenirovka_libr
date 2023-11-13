'''
sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7
'''

'''
#Не дорешено
def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    res = 0
    perem = 0
    for i in intervals:
        a, b = i
        if i in intervals[:perem]:
            perem += 1
            continue
        for j in intervals[:perem]:
            c, d = j
            if a > c and b < d:
                perem += 1
                break
            if a < c and b<d:
                res += d - a
                perem += 1
                break
            if a < d and b > c:
                res += b - d
                perem += 1
                break
        else:
            res += b - a
            perem += 1
    return res
'''



def sum_intervals2(intervals):
    s, top = 0, float('-inf')
    for a, b in sorted(intervals):
        if top<a:
            top = a
        if top < b:
            s, top = s+b-top, b
    return s




def sum_of_intervals(intervals):
    intervals.sort()
    lim,res=intervals[0][0],0
    for i in range(len(intervals)):  
        res+=max(intervals[i][1],lim)-max(intervals[i][0],lim)
        lim=max(lim,intervals[i][1])
    return res

print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))





