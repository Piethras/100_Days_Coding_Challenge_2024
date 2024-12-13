import random

rock = '''
    _____
---  ____)
    (_____)
    (_____)
    (____)
--._(___)

'''

paper = ''' 
    _____
---' ____)___
      _______)
      ________)
     _______)
--.________)


'''

scissors = '''
    _____
---' ____)_____
      _________)
      __________)
     (____)
--.__(___)

 '''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you loss")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer choose: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You loss")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice > user_choice:
        print("You loss")
    elif computer_choice == user_choice:
        print("It's a draw")
