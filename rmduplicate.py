x= [9, 1, 4, 7, 8, 8, 54, 9, 8, 889, 0, 6, 5, 4, 6, 7, 8, 54, 4, 3, 56, 5, 47, 3]

#Remove Duplicates: Remove duplicate elements from a list.
print(list(set(x)))


# List Comprehension: Create a new list by performing operations on each element of an existing list.
y = []
for i in x:
  if i > 5:
    y.append(i)
    x.remove(i)
print(y)


#List Slicing: Extract specific elements from a list using slicing.
if len(x) >= 5:
  z = x[4:-5]
  print(z)
  
a = 6
v= 5
print(a+v)

def calculator():
  while True:
    try:
      num1 = int(input("Enter an integer: "))
      num2 = int(input("Enter another integer: "))
      operator = input("Please enter an operator within +, -, /, ^: ")
      break
    except ValueError:
      print("Invalid input please enter an integer.")

  if operator == "+":
    add = num1 + num2
    print(add)
  elif operator == "-":
    sub = num1 - num2
    print(sub)
  elif operator == "*":
    multi = num1 * num2
    print(multi)
  elif operator == "/":
    if num2 != 0:
      div = num1 / num2
      print(div)
    else:
      print("Division by zero error ")
  elif operator == "^":
    power = num1 ** num2
    print(power)
  else:
    print("Invalid operator. Please enter a valid operator.")
    calculator()

  if input("Do you want to do another calculation? if yes enter 'y' \nor enter any key to exit: ").lower() == "y":
    calculator()