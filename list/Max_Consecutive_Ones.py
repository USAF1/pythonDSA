# Given a binary array nums, return the maximum number of consecutive 1's in the array.


from typing import List

#brute force

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    consitant = []
    count = 0
    for i in range(len(nums)):
        if(nums[i] == 1):
            count +=1
        elif(nums[i] !=1):
            consitant.append(count)
            count = 0
    consitant.append(count)
    count = 0
    if(len(consitant) == 0):
        return consitant[i]
    elif(len(consitant) < 0):
        return 0
    for i in range(0,len(consitant)):
        if(consitant[i] > count):
            count = consitant[i]
    return count


ans = findMaxConsecutiveOnes([1,1,0,1,1,1])

print(ans)