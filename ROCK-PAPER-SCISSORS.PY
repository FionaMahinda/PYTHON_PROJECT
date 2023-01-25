import random #defines a series of functions for generating or manipulating random integers
import os # A MODULE SUITABLE FOR AN OPERATITING SYSTEM
import re # helps look for patterns


def check_play_status():
  valid_responses = ['yes', 'no']# the response will be yes or no
  while True:
      try:
          response = input('Do you wish to play again? (Yes or No): ')
          if response.lower() not in valid_responses:
              raise ValueError('Yes or No only')

          if response.lower() == 'yes':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Thanks for playing!')
              exit()

      except ValueError as err:
          print(err)


def play_rps():# play rock,paper scissors
   play = True # once to intiate playing the game
   while play:
       os.system('cls' if os.name == 'nt' else 'clear')# accepting the player
       print('')
       print('Rock, Paper, Scissors - Shoot!')# one of the players response

       user_choice = input('Choose your weapon'
                           ' [R]ock], [P]aper, or [S]cissors: ')# the player chooses between rock paper and scissors

       if not re.match("[SsRrPp]", user_choice):
           print('Please choose a letter:')# the response is chosen as S or s, P or p and R or r 
           print('[R]ock, [P]aper, or [S]cissors')
           continue

       print(f'You chose: {user_choice}')

       choices = ['R', 'P', 'S']
       opp_choice = random.choice(choices)

       print(f'I chose: {opp_choice}')

       if opp_choice == user_choice.upper():# the result is a tie if bothe the player and the os make the same choice
           print('Tie!')
           play = check_play_status()
       elif opp_choice == 'R' and user_choice.upper() == 'S':
           print('Rock beats scissors, I win!')# as per the rules rock beats scissors
           play = check_play_status()
       elif opp_choice == 'S' and user_choice.upper() == 'P':
           print('Scissors beats paper! I win!')# scissors beats paper
           play = check_play_status()
       elif opp_choice == 'P' and user_choice.upper() == 'R':
           print('Paper beats rock, I win!')# paper beats rock
           play = check_play_status()
       else:
           print('You win!\n')# the outcome is set to three options: loose, win or tie
           play = check_play_status()# at the end of each game there is an option for a rematch or an option to end the game


if __name__ == '__main__':
   play_rps()
