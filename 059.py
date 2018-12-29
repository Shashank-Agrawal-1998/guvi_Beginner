def numofdigits(n):
    if n==0:
        return 0
    else:
        return 1 + numofdigits(n//10)

n = int(input())
if n==0:
    print(1)
elif n>0:
    result = numofdigits(n)
    print(result)