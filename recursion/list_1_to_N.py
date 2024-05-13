from typing import List

def printNos(x: int) -> List[int]:
    values = [] 
    if(x > 0):
        values = printNos(x-1)
        values.append(x)
    return values
    
# printNos(5)
ans = printNos(5);

print(ans)