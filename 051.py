def digitprint(n):
    if n!=0:
        digitprint(n//10)
        print(n%10, end=' ')

n = int(input())
digitprint(n)