def count_vowel():
  word = input("Enter a word or sentence: ")
  ans_1 = word.count("a")
  ans_2 = word.count("e")
  ans_3 = word.count("i")
  ans_4 = word.count("o")
  ans_5 = word.count("u")
  print(ans_1 + ans_2 + ans_3 + ans_4 + ans_5)

count_vowel()