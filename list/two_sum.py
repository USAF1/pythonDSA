# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
from typing import List

#Brute Force Solution.


# def twoSumBruteForce(nums: List[int], target: int) -> List[int]:
#     ans = []
#     n = len(nums)
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if(nums[i] + nums[j] == target):
#                 ans.append(i)
#                 ans.append(j)
#                 return ans

#     return ans



# ansBruteForce = twoSumBruteForce([2,7,11,15],9)

# print(ansBruteForce)

# optimal soultion


def twoSumOptimalForce(nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[nums[i]] = i



ansOptimalForce = twoSumOptimalForce([2,7,11,15],6)

print(ansOptimalForce)