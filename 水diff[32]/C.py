n = int(input())
B = []
A = list(map(int,input().split()))
mx = max(A)
mn = min(A)
if abs(mx)>abs(mn):
    ad = mx
else:
    ad = mn
idx = A.index(ad)
for a in A:
    B.append(a)
ans = []
for i,b in enumerate(B):
    ans.append((idx+1,i+1))
    B[i]+=ad
if B[0]<0:
    f =1
else:
    f = 0
for i in range(1,n):
    if f==0:
        ans.append((i,i+1))
        B[i]+=B[i-1]
    else:
        ans.append((i+1,i))
        B[i]+=B[i-1]
print(len(ans))
for a in ans:
    print(*a)