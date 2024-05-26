# 2149. Rearrange Array Elements by Sign
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
# Example 2:

# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].


from typing import List

#brute Force

def rearrangeArrayBruteForce(nums: List[int]) -> List[int]:
    negative = []
    positive = []

    for i in range(0, len(nums)):
        print(i % 2)
        if(nums[i] > 0):
            positive.append(nums[i])
        else:
            negative.append(nums[i])
    for j in range(0, len(nums)):
        if( j % 2 == 0):
            nums[j] = positive[j //2]
        else:
            nums[j] = negative[j // 2]
    return nums


print(rearrangeArrayBruteForce([3,1,-2,-5,2,-4]))


# optimal solution

def rearrangeArrayOptimal(nums: List[int]) -> List[int]:
    new_arr = [0] * len(nums)
    positive = 0
    negative = 1
    for i in range(0, len(nums)):
        if(nums[i] > 0):
            new_arr[positive] = nums[i]
            positive +=2
        else:
            new_arr[negative] = nums[i]
            negative +=2
    return new_arr


print(rearrangeArrayOptimal([3,1,-2,-5,2,-4]))