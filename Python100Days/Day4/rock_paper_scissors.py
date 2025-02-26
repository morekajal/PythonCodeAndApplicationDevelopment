"""
3 Simple Rules :
1. Rock Wins against Scissors
2. Scissors wins against Paper
3. Paper wins against Rock

- The starts by asking you to type 0:Rock, 1:Paper and 2:Scissor
- Your opponent is Computer which will randomly make choices and based on described rules - one will WIN!

"""


import random

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

# print(paper)
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : "))
if user_choice >=0 and user_choice <= 2:
      print(game_images[user_choice])

computer_choice = random.randint(0, 2)
# print(f"Computer choose : {computer_choice}")
print("Computer chose : ")
print(game_images[computer_choice])


### paper beats rock, scissors beats paper, and rock will beat scissors
### 1 beats 0, 2 beats 1, 0 beats 2

if user_choice >=3 or user_choice < 0:
      print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
      print("You Wins!")
elif computer_choice == 0 and user_choice == 2:
      print("You Lose!")
elif computer_choice > user_choice:
      print("You Lose!")
elif user_choice > computer_choice:
      print("You Win!")
elif computer_choice == user_choice:
      print("It's a Draw!")


