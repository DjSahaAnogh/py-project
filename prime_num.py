def check_prime():
  while True:
    try:
      num = int(input("Enter a number: "))
      break
    except ValueError:
      print("Invalid input! Please try again.")
    break
  
  for i in range(2, num):
    if num % i == 0:
      print(f"{num} is not a prime number.")
      break
  else:
    print(f"{num} is a prime number.")

  if input("Do you want use it again? If yes enter 'y' \nor enter any key to exit: ").lower() == "y":
    check_prime()


#check_prime()


a = True
b = True
if not a:
  print("Ok")
