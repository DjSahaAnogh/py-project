import random
from madlib import *

def guess(x):
  rand_num = random.randint(1, x)
  guess = 0
  while guess != rand_num:
    guess = int(input(f"Guess a number a between 1 and {x}: "))
    if guess < rand_num:
      print("Sorry, you guessed too low.")
    elif guess > rand_num:
      print("Sorry, you guessed too high.")
  print("Yay, You guessed the number correctly!!")


def computer_guess(x):
  low = 1
  high = x
  feedback = ""
  while feedback != "c":
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low # 'cuz low = high
    feedback = input(f"Is {guess} too high (h), too low (l) or correct (c): ").lower()
    if feedback == "h":
      high = guess - 1
    elif feedback == "l":
      low = guess + 1
  
  print(f"Yay, computer guessed your number, {guess}, correctly!!")


def game_chooes():
  game_name = input("Enter the game name (Madlib, Guess(User), Guess(Computer)): ")
  if game_name == "Madlib":
    madlib()
  elif game_name == "Guess(User)":
    x = int(input("Range: "))
    guess(x)
  elif game_name == "Guess(Computer)":
    x = int(input("Range: "))
    computer_guess(x)
  else:
    print("Sorry, that's all we have.")


game_chooes()