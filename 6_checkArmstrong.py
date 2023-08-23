from os import *
from sys import *
from collections import *
from math import *

def is_armstrong_number(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == number

num = int(input())
if is_armstrong_number(num):
    print("true")
else:
    print("false")
