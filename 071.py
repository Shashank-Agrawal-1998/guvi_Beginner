s = input()
s1 = list(s)
s1.reverse()
s1 = ''.join(s1)
if s==s1:
    print('yes')
else:
    print('no')