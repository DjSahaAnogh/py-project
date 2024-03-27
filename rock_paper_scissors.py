import random

def rps_game():
  user = input("What's your choise, 'r' for rock, 'p' for paper, 's' for scissors: \n")
  computer = random.choice(["r", "p", "s"])
  if is_win(user, computer) == True:
    print("yay! you win")
  else:
    print("You lost!")


def is_win(user, computer):
  if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
    return True
  

rps_game()