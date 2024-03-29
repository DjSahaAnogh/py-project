import random
import string
from words import words

def valid_word(words):
  word = random.choice(words)
  while "-" in word or " " in word:
    word = random.choice(words)
  return word.upper()


def hangman():
  word = valid_word(words)
  word_letters = set(word)
  alphabets = set(string.ascii_uppercase)
  used_letters = set()
  lives = 5

  # getting user input
  while len(word_letters) > 0 and lives > 0:
    print("You have ", lives, " lives and you have guessed these letters: ", " ".join(used_letters))
    word_list = [letter if letter in used_letters else "-" for letter in word]
    print("Current word: ", " ".join(word_list))

    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabets - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives -= 1
        print("Letter is not in the word.\n")
    elif user_letter in used_letters:
      print("You already used this letter. Please try again.\n")
    else:
      print("Invalid character. Please try again.\n")
  
  if lives == 0:
    print('You died, sorry. The word was ', word)
  else:
    print("You guessed the word '", word, "'.")


