n = int(input())
if n<=3:
    print('no')
else:
    f = 0
    for i in range(2,n):
        if n%i==0:
            f = 1
            break
    if f==0:
        print('no')
    else:
        print('yes')