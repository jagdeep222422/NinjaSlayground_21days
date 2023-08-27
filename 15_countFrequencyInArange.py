from typing import *
from collections import defaultdict

def countFrequency(n: int, m: int, edges: List[List[int]]):
    frequency = defaultdict(int)
    for edge in edges:
            frequency[edge] += 1
    return [frequency[i] for i in range(1, n+1)]
