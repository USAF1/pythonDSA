from typing import *

def revAr(arr, ind):
    n = len(arr)
    if ind == n //2:
        print(arr)
        return
    arr[ind], arr[n-1-ind] = arr[n-1-ind], arr[ind]
    revAr(arr, ind+1)


print(revAr([5, 7, 8, 1, 6, 3],6))
        