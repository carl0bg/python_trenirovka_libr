import timeit
# timeit — это простой интерфейс для быстрого измерения времени
# выполнения небольших блоков кода.
code_to_test = """
perem = 0
while (perem == 100):
   print('hello')
   perem +=1
"""
execution_time = timeit.timeit(code_to_test, number = 10000)
print(f"Execution time: {execution_time} seconds") #выводит результат во времени