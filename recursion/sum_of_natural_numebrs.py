from typing import List

def sumFirstN(n: int) -> int:
    if(n > 0):
        n = n + sumFirstN(n-1)
    return n
print(sumFirstN(3)) 