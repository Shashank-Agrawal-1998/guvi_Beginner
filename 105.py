n, k = map(int, input().strip().split())
z = k
digits_of_k = 0
while(z!=0):
    z = z//10
    digits_of_k = digits_of_k + 1
result = (n*(10**digits_of_k)) + k
print(result)