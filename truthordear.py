import random

def truth_or_dear():
  loop_range = random.choice([random.randint(0, 25)])
  x = 0
  while x != loop_range:
    x += 1
    global ans
    ans = random.choice(["user", "computer"])
  
  if ans == "user":
    user_response = input("Truth or Dear? \n :")
    if user_response == "Truth":
      user_name = input("What's your name? ")
      print(f"Hello {user_name}!")
    else:
      print("Slap yourself!")
  else:
    computer_choice = random.choice(["Truth", "Dear"])
    if computer_choice == "Truth":
      print("I'm a computer! LOL!")
    else:
      print("Ouch! I had to slapped myself.")


truth_or_dear()