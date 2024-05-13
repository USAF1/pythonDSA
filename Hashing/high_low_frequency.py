from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    simple = [0]*len(v)
    for i in range(len(v)):
        simple[v[i]] += 1
    return simple

print(getFrequencies([1, 2, 3, 1, 1, 4,6,10])) 