n = int(input())
L = list(input())
R = list(input())
mod = 1000000007
if n==1:print(3);exit()
ans = 3 if R[0]==L[0] else 6
for i in range(1,n):
    if L[i-1]==R[i-1]:
        if L[i]==R[i]:
            ans *=2
        else:
            ans *=2
    else:
        if L[i]!=L[i-1]:
            if L[i]==R[i]:
                continue
            else:
                ans *= 3
    ans %=mod
print(ans)