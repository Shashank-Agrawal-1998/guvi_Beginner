n = int(input())
numofdigits = 0
while(n!=0):
    n = n//10
    numofdigits += 1
print(numofdigits)