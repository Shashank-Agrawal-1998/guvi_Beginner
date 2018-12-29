s = input()
numchar = 0
for i in range(len(s)):
    if 48<=ord(s[i])<=57:
        numchar = numchar + 1
print(numchar)