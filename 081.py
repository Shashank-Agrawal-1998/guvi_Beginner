diff = []
while True:
    nm = input().strip()
    if nm=='':
        break
    else:
        n,m = map(int, nm.split())
        diff.append(m-n)
for i in diff:
    print(i)