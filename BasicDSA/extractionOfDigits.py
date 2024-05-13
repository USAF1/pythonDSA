import math

def printnum(num):
    count = 0
    # n = num
    x = 0
    while(num > 0):
        x = (x * 10) + num%10
        print(num%10, end="")
        num = num//10
        count = count +1
    print(count)
    # print(x)


def printnumm(num):
    return int(math.log10(num)) + 1

 
# print(printnumm(4329)) 
# 4321
printnum(1234000)

# TC (O(long10N))
# SC(O(1))