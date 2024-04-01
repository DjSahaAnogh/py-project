from madlib import *
from rock_paper_scissors import rps_game
from guess_the_num import *
from hangman import hangman



def game_chooes():
  game_name = input("Enter the game name (Madlib, Guess(User), Guess(Computer), Rps, Hangman): ")
  name = game_name.capitalize()
  if name == "Madlib":
    madlib()
  elif name == "Guess(User)":
    x = int(input("Range: "))
    guess(x)
  elif name == "Guess(Computer)":
    x = int(input("Range: "))
    computer_guess(x)
  elif name == "Rps":
    rps_game()
  elif name == "Hangman":
    hangman()
  else:
    print("Sorry, that's all we have.")


game_chooes()