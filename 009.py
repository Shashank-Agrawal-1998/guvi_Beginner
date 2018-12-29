n,k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
sum = 0
for i in range(k):
    sum = sum + arr[i]
print(sum)