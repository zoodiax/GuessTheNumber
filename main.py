import random


EASY = 10
HARD = 5

"""Compare the output of the two numbers: 0 == Win, 1 == Too High, 2 == Too Low"""
def compare(computer_num, player_num):
  if computer_num == player_num:
    return 0
  elif computer_num < player_num:
    return 1
  else:
    return 2


all_numbers = []


for i in range (1,101):
  all_numbers.append(i)

has_won = False
computer_number = random.choice(all_numbers)
print(f"Pssst, the correct number is: {computer_number}")

level = input("Press 'e' for easy and 'h' for a hard level ")
if level== "e":
  attempts = EASY
else:
  attempts = HARD

while attempts > 0:
  print(f"\n You have {attempts} attempts left:")
  player_number = int(input("Guess a number between 0 and 100 "))
  print(f"You choose {player_number}")
  comparison = compare(computer_number, player_number)
  if comparison == 0:
    attempts = -1
  elif comparison == 1:
    print("Your guess is too high")
    attempts -= 1
  else:
    print("Your guess is too low")
    attempts -=1

if attempts == -1:
  print("\nYou win")

else: 
  print("\nYou loose")

