from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/play', methods = ['POST'])
def play():
   player_choise = request.form['choice']
   choices = ['rock', 'paper', 'scissors']
   computer_choise = random.choice(choices)

   if player_choise == computer_choise:
      result = 'It is a tie!'
   elif((player_choise == 'rock' and computer_choise == 'scissors') or (player_choise == 'paper' and computer_choise == 'rock') or (player_choise == 'scissors' and computer_choise == 'paper')):
      result = 'You win!'
   else:
      result = 'You lose!'

   return render_template('result.html', player = player_choise, computer = computer_choise, result = result)

if __name__ == '__main__':
   app.run(debug = True)