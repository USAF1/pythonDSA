# Problem statement
# Given an array ‘arr’ of size ‘n’ find the largest element in the array.



# Example:

# Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

# Output: 5

# Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.


from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    largest_element = arr[0]
    for i in range(len(arr)):
        if(arr[i] > largest_element):
            largest_element  =arr[i]
    return largest_element

ans = largestElement([1, 2, 3, 4, 5], 5)

print(ans)
print(float("inf"))