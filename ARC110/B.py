n = int(input())
T = input()
if n==1:
    if T=='1':
        print(2*pow(10,10));exit()
if n==2:
    if T=='11':
        print(pow(10,10));exit()
    elif T=='10':
        print(pow(10,10));exit()
    elif T=='01':
        print(pow(10,10)-1);exit()
    else:
        print(0);exit()
    
cnt = 0
f = True
idx = -1
for i in range(n-2):
    if T[i]=='1':
        if T[i+1]=='1':
            if T[i+2]=='0':
                continue
            else:
                f = False
                break
        else:
            if T[i+2]=='1':
                continue
            else:
                f = False
                break
    else:
        if T[i+1]=='1':
            if T[i+2]=='1':
                continue
            else:
                f = False
                break
        else:
            f = False
            break
if not f:print(0);exit()

if T[:3]=='110':
    if n%3:
        tmp = n//3
    else:
        tmp = n//3-1
    print(pow(10,10)-tmp)
elif T[:3]=='101':
    n-=2
    if n%3:
        tmp = n//3
    else:
        tmp = n//3-1
    print(pow(10,10)-1-tmp)
else:
    n-=1
    if n%3:
        tmp = n//3
    else:
        tmp = n//3-1
    print(pow(10,10)-1-tmp)
