def tpl_sort(s):
    tupl = tuple(s)
    for per in tupl:
        if type(per) is not int:
            return tupl
    print('hel')
    return sorted(tupl)


print(tpl_sort([1000, 45.3, 40, 30]))