x = int(input())
a = x//11
b = x%11
if b:
    if b>6:
        print(2*a+2)
    else:
        print(2*a+1)
else:
    print(2*a)