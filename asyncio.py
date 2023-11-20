import asyncio

'''
async def send_one() -> None:
   n = 0
   while True:
      await asyncio.sleep(1)
      n+=1
      if n/3 == int(n/3):
         print(f'прошло еще 3 секунды')
      print(f'прошло {n} секунд')
'''

'''
async def send_one() -> None:
   n = 0
   while True:
      await asyncio.sleep(1)
      n+=1
      print(f'прошло {n} секунд')

async def send_three():
   while True:
      await asyncio.sleep(3)
      print('прошло еще 3 сек')


async def main():
   task_1 = asyncio.create_task(send_one())
   task_2 = asyncio.create_task(send_three())

   await task_1
   await task_2


if __name__ == '__main__':
   asyncio.run(main())

'''



async def send_time(sec: int):
   while True:
      await asyncio.sleep(sec)
      print(f'Прошло {sec} секунд')


#print(send_time(2), send_time(5), sep = '\n')

async def main():
   task_1 = asyncio.create_task(send_time(2)) #различные обьекты корутин
   task_2 = asyncio.create_task(send_time(5))

   await task_1
   await task_2



if __name__ == '__main__':
   asyncio.run(main())