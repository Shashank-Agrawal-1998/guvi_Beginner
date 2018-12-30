def printfactors(n,i):
    if i<=n:
        if n%i == 0:
            print(i, end=' ')
        printfactors(n,i+1)

n = int(input())
printfactors(n,1)