# 229. Majority Element II
# Medium
# Topics
# Companies
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

from typing import List

        


def majorityElements(nums: List[int])->List[int]:
    numsLength = len(nums)
    if(numsLength == 1):
        return nums
    hash_tab = dict()
    numsArr = []
    for i in range(0,numsLength):
        if(nums[i] in hash_tab):
            hash_tab[nums[i]] += 1
        else:
            hash_tab[nums[i]] = 1
    for key,value in hash_tab.items():
        if(value >= numsLength//3):
            numsArr.append(key)

    return numsArr




print(majorityElements([1,3])) 
print(2//3)