from os import *
from sys import *
from collections import *
from math import *

def printPattern(n):
    #Write your code here
    for i in range(1, n+1):
      print(" " * (n - i), end="")
      print("*" * (2 * i - 1))
