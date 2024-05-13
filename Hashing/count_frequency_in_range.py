
from typing import List

def countFrequency(n: int, m: int, edges: List[List[int]]):
   mylst = [0] * n
   for x in edges:
        if x > n:
            continue
        mylst[x - 1] += 1
   return mylst

print(countFrequency(10, 14,[11,14,8,3,12,14,1,7,4,3]))