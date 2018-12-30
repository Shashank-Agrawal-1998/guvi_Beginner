arr = list(map(int, input().strip().split()))
min = arr[0]
for i in range(10):
    if arr[i] < min:
        min = arr[i]
print(min)