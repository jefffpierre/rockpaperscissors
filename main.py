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

#Write your code below this line 👇
choice = int(input("Please enter 0 for Rock, 1 for Paper or 2 for Scissors ")) #Stored the user's input.
choice2 = random.randint(0,2)
print("\nLets Roll!")

if choice == 0:
  print(rock)
  if choice2 == 0:
    print("Computer says:")
    print(rock)
    print("Both rock, try again!")
  elif choice2 == 1:
    print("Computer says:")
    print(paper)
    print("Paper! You lose!")
  elif choice2 == 2:
    print("Computer says:")
    print(scissors)
    print("Scissors! Aw No :( You Win!")
elif choice == 1:
  print(paper)
  if choice2 == 0:
    print("Computer says:")
    print(rock)
    print("Rock! Aw No :( You Win!")
  elif choice2 == 1:
    print("Computer says:")
    print(paper)
    print("Both paper, try again")
  elif choice2 == 2:
    print("Computer says:")
    print(scissors)
    print("Ha Scissors! Sucka! You lose!")
elif choice == 2:
  print(scissors)
  if choice2 == 0:
    print("Computer says:")
    print(rock)
    print("Rock! Sucka! You lose.")
  elif choice2 == 1:
    print("Computer says:")
    print(paper)
    print("Paper, dangit, you win!")
  elif choice2 == 2:
    print("Computer says:")
    print(scissors)
    print("Both scissors, try again!") 
else:
  print("Did you choose 0, 1 or 2? Please try again. :)")

print("\nThis was great, let's do it Again!")