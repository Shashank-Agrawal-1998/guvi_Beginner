result = []
while True:
    nom = input().strip()
    if nom=='':
        break
    else:
        n,o,m = map(str, nom.split())
        if o=='/':
            r = int(n)//int(m)
            result.append(r)
        elif o=='%':
            r = int(n)%int(m)
            result.append(r)
for i in result:
    print(i)