s = input()
flag = 1
for i in range(len(s)):
    if not(s[i]=='0' or s[i]=='1'):
        flag=0
        break
if flag==0:
    print('no')
else:
    print('yes')