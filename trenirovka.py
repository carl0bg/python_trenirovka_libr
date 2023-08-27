import operator
#import functools
from functools import lru_cache
import requests #библиотека для бысрой работы с запросами http
# numbers = [1, 2, 3, 4, 5, 6]
# summed = functools.reduce(operator.add, numbers)
# product= functools.reduce(operator.mul, numbers)
# print(summed)
# print(product)

# @lru_cache(maxsize = 32)
# def get_with_cache(url):
#     try:
#         r = requests.get(url)
#     except:
#         return "Not found"
    
# for url in ["https://google.com/",
#             "https://martinheinz.dev/",
#             "https://reddit.com/"]:
#     get_with_cache(url)

#print(get_with_cache.cache_info())

res = requests.get("https://skillbox.ru") #получаем информацию о страницы
content = res.content #поулучаем контент страницы
content = res.text #удобночитаем информация страницы
print(content) 