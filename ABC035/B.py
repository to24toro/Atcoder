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
    print(abs(cur-cnt))