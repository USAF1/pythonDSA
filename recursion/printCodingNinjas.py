from  typing import *

def printNtimes(n: int) -> List[str]:
    result = []
    if(n > 0):
        result  = printNtimes(n-1)
        result.append("Coding Ninjas")
    return result

print(printNtimes(3)) 