a,b = map(int, input().strip().split())
for i in range(a+1,b):
    flag = 0
    for j in range(2, i):
        if i%j==0:
            flag=1
    if flag==0 and i>1:
        print(i, end=' ')