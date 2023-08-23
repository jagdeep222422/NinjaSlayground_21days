from os import *
from sys import *
from collections import *
from math import *

def termsOfAP(x):
    # Write your code here
    # Return a list of integers
    ans = []
    temp = 0
    n = 1
    count = 0  
    while count != x:
        temp = 3 * n + 2
        if temp % 4 != 0:
            ans.append(temp)
            count += 1
        n += 1
    return ans
