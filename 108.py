n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
f = 0 
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            f = 1
    if f==0:
        break
print(arr[k-1])