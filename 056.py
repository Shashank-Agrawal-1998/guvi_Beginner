s = input()
alpha = 0
num = 0
for i in range(len(s)):
    if 48<=ord(s[i])<=57:
        num = 1
    if 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122:
        alpha = 1
    if num==1 and alpha==1:
        break
if num==1 and alpha==1:
    print('Yes')
else:
    print('No')