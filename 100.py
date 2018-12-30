n = int(input())
if n==0:
    print(0)
elif n<0:
    n = n*(-1)
    pro = 1
    while(n!=0):
        pro = pro * (n%10)
        n = n//10
    print(pro*(-1))
else:
    pro = 1
    while(n!=0):
        pro = pro * (n%10)
        n = n//10
    print(pro)