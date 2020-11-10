S = input()
T = int(input())
x = 0
y = 0
cnt = 0
for s in S:
    if s=='U':
        y += 1
    elif s =='D':
        y-=1
    elif s =='R':
        x += 1
    elif s =='L':
        x -=1
    else:
        cnt += 1
cur = abs(x)+abs(y)
if T==1:
    print(cur+cnt)
else:
    tmp = cnt-abs(x)-abs(y)
    if tmp>0:
        if tmp%2==0:
            print(0)
        else:
            print(1)
    else:
        print(abs(cur-cnt))