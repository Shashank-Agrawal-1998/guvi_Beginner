s = input()
word = 0
for i in range(len(s)):
    if s[i]==' ' and s[i-1]!=' ':
        word = word + 1
word = word + 1
print(word)