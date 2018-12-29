n = int(input())
arr = list(map(int, input().strip().split()))
low = arr[0]
high = arr[0]
for i in range(n):
    if arr[i] < low :
        low = arr[i]
    if arr[i] > high:
        high = arr[i]
print(low,high)