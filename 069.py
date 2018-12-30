n, m = map(int, input().strip().split())
diff = abs(n-m)
if diff%2==0:
    print('even')
else:
    print('odd')