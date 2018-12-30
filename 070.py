import math

n = int(input())
if n<=0:
    print(1)
else:
    a = int(math.log2(n)) + 1
    a = 2**a
    print(a)