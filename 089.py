st = input()
s = list(st)
f = 0
for i in range(len(s)-1):
    for j in range(len(s)-i-1):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
            f = 1
    if f==0:
        break
for i in s:
    print(i,end='')