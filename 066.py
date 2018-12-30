n = int(input())
if n<=1:
    print('no')
else:
    f = 0
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            f=1
            break
    if f==0:
        print('yes')
    else:
        print('no')