from typing import List

def printDivisors(n: int) -> List[int]:
    numbers = []
    for i in range(1,n +1,1):
        if(n%i == 0):
            numbers.append(i)
    return numbers

print(printDivisors(5))