t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
A1,A2 = a1*t1,a2*t2
B1,B2 = b1*t1,b2*t2
if A1+A2==B1+B2:
    print('infinity');exit()
if A1>B1:
    if A2>B2:
        print(0);exit()
    else:
        if A1+A2>B1+B2:
            print(0);exit()
else:
    if A2<B2:
        print(0);exit()
    else:
        if A1+A2<B1+B2:
            print(0);exit()
ans = 0
diff = abs(B1+B2-A1-A2)
add = abs(A1-B1)//diff
add*=2
if diff >=abs(A1-B1):
    add = 1
else:
    if abs(A1-B1)%diff:
        add += 1

print(ans + add)

