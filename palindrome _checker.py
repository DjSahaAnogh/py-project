s = input("Please enter a word: ")
new_s = s[::-1]
if s == new_s:
  print(f"{s} is a palindrome word.")
else:
  print(f"{s} is not a palindrome word.")