x = int(input())
y = (x//11)*2
if x%11==0:
    print(y)
else:
    if x%11<=6:
        print(y+1)
    else:
        print(y+2)