def madlib1():
    madlib_1_adjective = input("Adjective: ")
    madlib_1_noun = input("Noun: ")
    madlib_1_verb = input("verb: ")
    madlib_1_body_part = input("Body part: ")
    madlib1 = f"Last weekend, we went on a {madlib_1_adjective} picnic. We packed a basket full of delicious {madlib_1_noun}. Suddenly, a swarm of bees {madlib_1_verb} around our food! We ran away as fast as our little {madlib_1_body_part} could carry us."
    print(madlib1)


def madlib2():
    madlib_2_noun = input("Verb: ")
    madlib_2_adverb = input("Verb: ")
    madlib_2_celebrity = input("Adjective: ")
    madlib_2_verb = input("Adjective: ")
    madlib2 = f"Last night, I went to the movies to see a new {madlib_2_noun}. The popcorn was {madlib_2_adverb} salty, and my drink was flat. To top it all off,  {madlib_2_celebrity}  unexpectedly walked in and sat right next to me! I was so nervous, I accidentally {madlib_2_verb} my popcorn all over them!"
    print(madlib2)


def madlib():
  i = input("Enter the madlib number(1-2): ")
  if i == "1":
    madlib1()
  else:
    madlib2()