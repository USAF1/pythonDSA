def func(n):
    if(n>1):
        n = n * func(n-1)
    return n

print(func(5))