rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
human_play = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(f'You play {options[human_play]}')
import random
computer_play = random.randint(0,2)
print(f'Computer play {options[computer_play]}')

if human_play == computer_play:
    print('It\'s a Draw')
elif human_play == 0 and computer_play == 1:
    print('You lose!')
elif human_play == 0 and computer_play == 2:
    print('You win!')
elif human_play == 1 and computer_play == 0:
    print('You win!')
elif human_play == 1  and computer_play == 2:
    print('You lose!')
elif human_play == 2 and computer_play == 0:
    print('You lose!')
elif human_play == 2 and computer_play == 1:
    print('You win!')
elif int(human_play) >= 3:
    print('You lose...')
