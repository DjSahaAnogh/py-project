import random

def guess(x):
  rand_num = random.randint(1, x)
  guess = 0
  while guess != rand_num:
    guess = int(input(f"Guess a number a between 1 and {x}: 5"))
    if guess < rand_num:
      print("Sorry, you guessed too low.")
    elif guess > rand_num:
      print("Sorry, you guessed too high.")
  print("Yay, You guessed the number correctly!!")


guess(10)