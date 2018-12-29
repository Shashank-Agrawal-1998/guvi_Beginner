n = int(input())
arr = list(map(int, input().strip().split()))
sum = 0
for i in range(n):
    sum += arr[i]
print(sum//n)