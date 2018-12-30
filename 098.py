n = int(input())
arr = list(map(int, input().strip().split()))
index = None
for i in range(n-1):
    if arr[i] > arr[i+1]:
        index = i
        break
print(index)