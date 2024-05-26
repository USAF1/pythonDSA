# 53. Maximum Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

from typing import List


# optimal Kadane's algorithm

def maxSubArrayOptimal(nums: List[int]) -> int:
    max_sum = 0
    x = 0
    for i in range(0,len(nums)):
        x = x+nums[i]
        max_sum  =max(max_sum,x)
        if(x <= 0):
            x = 0
    return max_sum



print(maxSubArrayOptimal([5,4,-1,7,8]))


x  = [1]
print(len(x))