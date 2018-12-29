a,b = map(int, input().strip().split())
a = a^b
b = a^b
a = a^b
print(a,b)