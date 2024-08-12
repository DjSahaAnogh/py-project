def fibonacci_sequence():
  while True:
    try:
      num_of_term = int(input("Enter number of terms: "))
      break
    except ValueError:
      print("Invalid input! Please enter an integer.")
  term_1 = 0
  term_2 = 1
  while num_of_term:
    term_1, term_2 = term_2, (term_1+term_2)
    print(term_1)
    num_of_term -=1

  if input("Do you want to use it again (y) \nor enter any key to stop: ").lower() == "y":
    fibonacci_sequence()

fibonacci_sequence()
