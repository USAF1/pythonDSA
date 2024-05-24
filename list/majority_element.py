# 169. Majority Element
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List

#brute-force solution

def majorityElemmentBruteForce( nums: List[int]) -> int:
    ans  = 0
    n = len(nums)
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if(nums[i] == nums[j]):
                count +=1
        if(count > n//2):
            ans = nums[i]
        return ans
    return ans



print(majorityElemmentBruteForce([2,2,1,1,1,2,2]))

# Better solution

def majorityElemmentBetter( nums: List[int]) -> int:
    ans  = 0
    hash_table = dict()
    for i in range(0,len(nums)):
        if(nums[i] in hash_table):
            hash_table[nums[i]] += 1
        else:
            hash_table[nums[i]] = 1
    for k,h in hash_table.items():
        if(h > len(nums)//2):
            ans = k
    return ans



print(majorityElemmentBetter([2,2,1,1,1,2,2]))

#optimal Solution

def majorityElemmentOptimal( nums: List[int]) -> int:
    candidate = nums[0]
    counter = 1

    for i in range(1,len(nums)):
        if(nums[i] == candidate):
            counter +=1
        else:
            counter -= 1
        if(counter == 0):
            candidate = nums[i]
            counter = 1
    return candidate



print(majorityElemmentOptimal([2,2,1,1,1,2,2]))