# Problem statement
# You are given a sorted integer array 'arr' of size 'n'.



# You need to remove the duplicates from the array such that each element appears only once.



# Return the length of this new array.



# Note:
# Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory. 


# For example:
# 'n' = 5, 'arr' = [1 2 2 2 3].
# The new array will be [1 2 3].
# So our answer is 3.



# def removeDuplicates(arr,n):
#     unique = 0
#     for i in range(len(arr)-1):
#         if(arr[i] != arr[i+1]):
#             unique +=1
#     return unique
# ans = removeDuplicates([1 ,2 ,2 ,2 ,3],4)

#brute force

def removeDuplicates(arr,n):
    my_dict = dict()
    for i in arr:
        my_dict[i] = 0
    j = 0
    for k in my_dict:
        j +=1
    return j
ans = removeDuplicates([1, 2, 2 ,3, 3, 3, 4, 4, 5, 5],4)
print(ans)


#opitmal

def removeDuplicatesOPT(arr,n):
    i = 0
    j = i+1

    while j < len(arr):
        if(arr[j] != arr[i]):
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
        j+=1
    return i+1
ansOPT = removeDuplicatesOPT([1, 2, 2 ,3, 3, 3, 4, 4, 5, 5],4)
print(ansOPT)