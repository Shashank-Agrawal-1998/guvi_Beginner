n = int(input())
m = n
k = 0
while(m!=0):
    k = k*10 + m%10
    m = m//10
if n==k:
    print('yes')
else:
    print('no')