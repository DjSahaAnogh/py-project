#Simple Calculator: Create a basic calculator that performs addition, subtraction, multiplication, and division.

def calculator():
  while True:
    try:
      num1 = int(input("Enter the first number: "))
      op = input("Enter an operator(+, -, *, /): ")
      num2 = int(input("Enter the second number: "))
      break
    except ValueError:
      print("Invalid input!! Please try again.")
      calculator()
 
  if op == "+":
     print(num1 + num2)
  elif op == "-":
     print(num1 - num2)
  elif op == "*":
     print(num1 * num2)
  elif op == "/" and num2 != 0:
     print(num1 / num2)
     if num2 == 0:
        print("Can't divide by zero.")
  else:
     print("Invalid operator.")
     calculator()
  
  if input("Do you want to use it again? If yes enter 'y' \nor enter any key: ").lower() == 'y':
     calculator()


calculator()
