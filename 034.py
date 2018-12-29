s = input()
line = 0
for i in range(len(s)):
    if s[i]=='.':
        line = line + 1
line = line + 1
print(line)