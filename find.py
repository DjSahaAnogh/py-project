# Find the Largest Number: Find the largest number in a list.
from random import randint, random

def find_larggest_num(num=[]):
  num.sort()
  print(num[-1])
i = [10, 5, 85 , 5465, 85 ,565 ,95 ,32 ,45, 55 ,956 ,95 ,95,959,56,69 ,96 ,96]

# def find_num():
#   n = 0
#   while n != len(num):
#     if n == len(num) - 1:
#       break
#     i, x = num[0+n], num[0+n+1]
#     if i>x:
#       lis = []
#       lis.insert(-1, i)
#       print(lis)
#     n += 1
  
find_larggest_num(i)