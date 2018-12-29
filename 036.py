s = input()
spechar = 0
for i in range(len(s)):
    if not(48<=ord(s[i])<=57 or 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122 or s[i]==' '):
        spechar = spechar + 1
print(spechar)