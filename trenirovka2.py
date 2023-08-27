from itertools import combinations

data = ['a', 'b', 'c']
lst = list(combinations(data, 2)) #комбинирует результаты
print(lst) #[('a', 'b'), ('a', 'c'), ('b', 'c')]
