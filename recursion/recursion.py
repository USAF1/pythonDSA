# def func(i,n):
#     if(i > n):
#         return
#     print(i)
#     func(i+1,n)

# func(1,7)



def funcreverse(i,n):
    if(i>n):
        return
    print(n)
    funcreverse(i+1,n-1)

funcreverse(1,7)