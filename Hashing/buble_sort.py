import array
from typing import List

def bubbleSort(x:List[int]):
    for i in range(len(x)-2,-1,-1):
        for j in range(0, i+1):
            if(x[j] > x[j+1]):
                x[j],x[j+1] = x[j+1],x[j]
    return x


print(bubbleSort([8,3,77,3,1,9,5])) 