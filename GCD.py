# Greatest Common Divisor (GCD): Find the GCD of two numbers using the Euclidean algorithm.

def computeGCD(num1, num2):
  while num2 :
    num1, num2 = num2, (num1 % num2)
  print(num1)

computeGCD(200, 400)
