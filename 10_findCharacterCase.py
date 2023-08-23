from os import *
from sys import *
from collections import *
from math import *

def findCase(ch):
    # Write your code here
    # Return an integer denoting the answer
    if ch>='A' and ch<='Z':
        return 1
    elif ch>='a' and ch<='z':
        return 0
    else:
        return -1       
