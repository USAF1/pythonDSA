# 75. Sort Colors
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

#Better Solution

from typing import List

def sortColorsBetterSolution(nums: List[int]) -> None:

    n = len(nums)
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(0, n):
        if nums[i] == 0:
            cnt1 += 1
        elif nums[i] == 1:
            cnt2 += 1
        else:
            cnt3 += 1
    for i in range(0, cnt1):
        nums[i] = 0
    for i in range(cnt1, cnt1 + cnt2):
        nums[i] = 1
    for i in range(cnt1 + cnt2, cnt1 + cnt2 + cnt3):
        nums[i] = 2

    return nums


ans = sortColorsBetterSolution([2,0,2,1,1,0])

print(ans)

