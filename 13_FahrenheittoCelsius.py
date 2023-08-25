from os import *
from sys import *
from collections import *
from math import *

def fahrenheitToCelsius(s,e,w):
    gs = []
    for i in range(s, e + 1, w):
        k = int((i - 32) * 5 / 9)
        gs.append([i, k])
    return gs
