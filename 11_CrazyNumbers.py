from os import *
from sys import *
from collections import *
from math import *

def numberPattern(n):
    num = 1
    ans = []
    for i in range(n - 1, -1, -1):
        temp = []
        for j in range(n):
            if j < i:
                temp.append(-1)
            else:
                temp.append(num)
                num += 1
                if num == 10:
                    num = 1
        ans.append(temp)
    return ans
