a,b = map(int, input().strip().split())
for n in range(a+1, b):
    m = n
    numofdigits = 0
    while(m!=0):
        m = m//10
        numofdigits = numofdigits + 1
    m = n
    k = 0
    while(m!=0):
        k = k + (m%10)**numofdigits
        m = m//10
    if k==n:
        print(n, end=' ')