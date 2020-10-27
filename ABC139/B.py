a,b = map(int,input().split())
c = 0
ans = 1

for _ in range(30):
    if ans>=b:
        print(c);exit()
    ans +=a-1
    c+=1