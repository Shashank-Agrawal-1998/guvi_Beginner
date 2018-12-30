n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
c = 0
for i in range(n):
    if arr[i]%2==1:
        c += 1
    if c==k:
        print(arr[i])
        break