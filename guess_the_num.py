import random
from madlib import *
from rock_paper_scissors import rps_game

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

