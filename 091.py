l, b, h = map(int, input().strip().split())
sur_area  = 2*(l*b + b*h + l*h)
vol = l*b*h
print(sur_area, vol)