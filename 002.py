n = input()
try:
    n = float(n)
    if n>=0:
        if n%2==0:
            print("Even")
        elif n%2==1:
            print("Odd")
        else:
            print("Invalid")
    else:
        print("Invalid")
except:
    print("Invalid")