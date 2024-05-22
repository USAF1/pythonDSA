# Problem statement
# You are given an array 'a' of size 'n' and an integer 'k'.



# Find the length of the longest subarray of 'a' whose sum is equal to 'k'.



# Example :
# Input: ‘n’ = 7 ‘k’ = 3
# ‘a’ = [1, 2, 3, 1, 1, 1, 1]

# Output: 3

# Explanation: Subarrays whose sum = ‘3’ are:

# [1, 2], [3], [1, 1, 1] and [1, 1, 1]

# Here, the length of the longest subarray is 3, which is our final answer.




def longestSubarrayWithSumK(a: [int], k: int) -> int:
    final_arr = []
    opt_arr = []
    i = 0
    j = i+1
    while i< len(a):
        if(len(final_arr) < len(opt_arr)):
            final_arr = opt_arr
            opt_arr = []
        x = 0
        if(a[i]== k):
            opt_arr.append(k)
            i+=1
            j = i+1
            continue
        arr = a[i:j+1]
        x = sum(arr)
        if(x == k):
            opt_arr = a[i:j+1]
        i+=1
        j=i+1
    return final_arr


ans = longestSubarrayWithSumK([1, 2, 3, 1, 1, 1, 1],3)

print(ans)


#another solution


def longestSubarrayWithSumKk(a: [int], k: int) -> int:
    maxIndex = 0
    sum = 0
    index = 0
    for i in range(0, len(a)):
        sum = sum+a[i]
        index +=1
        if(sum == k):
            if(maxIndex < index):
                maxIndex = index
            index = 0
            sum = 0
    return maxIndex

ans = longestSubarrayWithSumKk([1,1,2,3,1,2,1,1,1,1],4)

print(ans)