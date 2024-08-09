# # Write a program that takes a number as input and prints whether it is even or odd.

def evenOrOdd():
  while True:
    try:
      number = int(input("Enter a number: "))
      break
    except ValueError:
      print("Invalid input. Please enter an integer!")
    
  if number % 2 == 0:
    print("It is an even number.")
  else:
    print("It is an odd number.")

evenOrOdd()

# previous version
# def evenOrOdd():
#   try:
#     input_num = int(input("Enter an number: "))
#   except(ValueError):
#     print("An error ocured!")
#     print("Program restarted!")
#     return True

#   test = input_num / 2
#   def check(arg):
#     num_str = str(arg)
#     decimal_index = num_str.find('.')

#     if decimal_index == -1:
#       # No decimal point, so no significant figures after it
#       return False

#     for char in num_str[decimal_index + 1:]:
#       if char != '0':
#         return True

#     return False
  

#   ans = check(test)
#   if ans:
#     print("It is an odd number.")
#   else:
#     print("It is an even number.")
  

# evenOrOdd()

