""" from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
per = Person('Alice', '18', 'Arz')
print(per.name, per.age, per.city) """ #Shift+Alt+A

""" from pathlib import Path
path = Path('c:\\Users\\serka\\Downloads') #по определенным каталогам(путь)
for file in path.glob('*.docx'): #ищет обьекты которые docx
    print(file) """

