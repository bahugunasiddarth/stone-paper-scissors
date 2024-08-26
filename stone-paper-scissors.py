import random
import sys

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
game_image=[rock,paper,scissors]

user_choice =int(input("What do you choice? Type 0 for rock, 1 for paper, 2 for scissors\n "))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
  sys.exit()
else:
    print("You chose:")
    print(game_image[user_choice])
    
 

computer_choice = random.randint(0,2)
print(f"Computer choice {computer_choice}")
print(game_image[computer_choice])


if user_choice == computer_choice:
    print ("It's a tie!")

elif(user_choice== 0 and computer_choice==2)or\
        (user_choice== 1 and computer_choice==0)or\
        (user_choice== 2 and computer_choice==1):
    print("You Win")
else:            
    print ("Computer wins!")       


