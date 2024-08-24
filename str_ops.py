def srt_ops():
  while True:
    text = input("Please enter a sentence: ")
    for i in list(text):
      if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        print("You have entered an integer along with a \nstring, which is not exceptable. Please try again.")
        text = input("Please enter a sentence: ")
      
    break
  
  print("Your text is", (text))
  print("This is your text in UPPER case:\n", text.upper())
  print("This is your text in lower case:\n", text.lower())
  print("This will capitalize your text:\n", text.capitalize())
  


srt_ops()