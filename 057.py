n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
repeat = 0
for i in range(n):
    if arr[i]==k:
        repeat += 1
print(repeat)