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
import random
#Write your code below this line 👇

while True:
    choice = input(
        "Do you want to Start(type 'start') or Quit('type 'quit'): ")
    if choice == 'start':
        print("********* Player1 Turn *********")
        Player1 = input(
            "What do you want to choose: Type 'rock', 'paper', or 'scissor' : \n"
        )
        if Player1 == 'rock':
            print(rock)
        elif Player1 == 'paper':
            print(paper)
        elif Player1 == 'scissor':
            print(scissors)
        print("********* Computer Turn *********")
        computer = random.randint(0, 2)
        if computer == 0:
            print(rock)
        elif computer == 1:
            print(paper)
        elif computer == 2:
            print(scissors)

        if Player1 == 'rock' and computer == 2:
            print("Player1 Wins!")
        elif Player1 == 'paper' and computer == 2:
            print("You lose!")
        elif Player1 == 'scissor' and computer == 0:
            print("You lose!")
        elif Player1 == "scissor" and computer == 1:
            print("Player1 Wins!")
        elif Player1 == 'paper' and computer == 0:
            print("Player1 Wins!")
        elif Player1 == 'rock' and computer == 1:
            print("You lose!")
        elif Player1 == computer:
            print('Draw!')
        else:
            print(
                "Invalid input! Please choose 'rock', 'paper', or 'scissor'.")
    elif choice == 'quit':
        break
    else:
        print("Please type 'start' to start or 'quit' to end the game! ")
