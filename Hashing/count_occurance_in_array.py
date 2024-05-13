import array
def findOccurance(arr):
    sample = [0]*122
    for i in range(len(arr)):
        ascii_Code = ord(str(arr[i]))
        sample[ascii_Code] +=1
    print(sample)
        

findOccurance([1,"a","b","A",0,4, "a"])