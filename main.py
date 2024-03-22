def game():
  name = input("Your name: ")
  verb1 = input("Verb: ")
  verb2 = input("Verb: ")
  adj1 = input("Adjective: ")
  adj2 = input("Adjective: ")
  madlib = f"Hello my name is {name}. I like {verb1} and {verb2}. {verb1} is so {adj1} \
 and I also {adj2} programming."
  print(madlib)

game()