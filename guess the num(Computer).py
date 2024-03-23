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


def game_chooes():
  game_name = input("Enter the game name: ")
  if game_name == "Madlib":
    madlib()
  elif game_name == "Guess(Computer)":
    x = int(input("Range: "))
    guess(x)
  else:
    print("Sorry, that's all we have.")


game_chooes()