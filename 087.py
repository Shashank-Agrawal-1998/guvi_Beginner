def gcd(n,m):
    if n==0:
        return m
    elif m==0:
        return n
    elif n%m==0:
        return m
    else:
        return gcd(m,n%m)

a,b = map(int, input().strip().split())
if a>b:
    result = gcd(a,b)
else:
    result = gcd(b,a)
print(result)