'''
if divisble by 3 print fizz
if divisble by 5 print buzz
if divisble by both 3 and 5 print fizzbuzz
else print the number
'''

def fizzbuzz(num):
  while True:
    if num % 3 != 0 and num % 5 != 0:
      print(num)
      break
    if num % 3 == 0 and num % 5 == 0:
      print('fizzbuzz')
      break
    if num % 3 == 0 or num % 5 == 0:
      if num % 3 == 0:
        print("fizz")
        break
      if num % 5 == 0:
        print("buzz")
        break


fizzbuzz(56)