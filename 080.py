def printodddigits(n):
    if n==0:
        return 0
    else:
        if (n%10)%2==1:
            printodddigits(n//10)
            print(n%10, end=' ')
        else:
            printodddigits(n//10)
    
n = int(input())
printodddigits(n)