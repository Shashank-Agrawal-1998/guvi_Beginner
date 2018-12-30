import math
a, d, n = map(float, input().strip().split())
sum = (n/2)*(2*a + (n-1)*d)
print(math.floor(sum))