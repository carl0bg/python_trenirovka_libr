import random
count_h = 0
count_c = 0

print('Hey! Welcome to the game Lets begin...\n')
keep_playing = True

while keep_playing:
   c_choise  = random.choice(['rock', 'paper', 'scissors'])
   print('the computer chooses' + c_choise)

   h_choise = random.choice(['rock', 'paper', 'scissors'])
   print('the human chooses'+ h_choise)

   if((h_choise == 'rock' and c_choise == 'scissors') or (h_choise == 'scissors' and c_choise == 'paper') or (h_choise == 'paper' and c_choise == 'rock')):
      print('Human wins!')
      count_h += 1
   elif (h_choise == c_choise):
      print('draw')
   else:
      print('Computer wins!')
      count_c += 1

   print('\nDo you want to play again?')
   answer = input()
   if answer == 'no':
      keep_playing = False
      print('Thanks for playing!')
      print(f'Computer score is {count_c}')
      print(f'Human score is {count_h}')

      print('\nOverall results:')
      if count_c>count_h:
         print("Better luck next time!\n")
      elif count_c == count_h:
         print("It is a draw\n")
      else:
         print('You win!')
         