n = int(input())
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
    print('yes')
else:
    print('no')