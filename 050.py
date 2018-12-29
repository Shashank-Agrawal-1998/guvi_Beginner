n = int(input())
ans = n&(n-1)
if ans == 0:
    print('yes')
else:
    print('no')