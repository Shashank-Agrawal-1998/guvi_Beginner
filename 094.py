n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
if 0<=k<n:
    print(arr[k-1])