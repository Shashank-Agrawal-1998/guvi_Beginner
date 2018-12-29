def sumofnaturals(k):
    if k==0:
        return 0
    else:
        return k + sumofnaturals(k-1)

k = int(input())
if k>=0:
    result = sumofnaturals(k)
    print(result)