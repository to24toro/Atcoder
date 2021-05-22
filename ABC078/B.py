n,m = map(int,input().split())
A = list(map(int,input().split()))
set_ = set(A)
B = list(map(int,input().split()))
a = [0]*(10**3+1)
b = [0]*(10**3+1)
for i in A:
    a[i]+=1
for j in B:
    b[j]+=1
ans = []
for i in range(1,10**3+1):
    if a[i]>0 and b[i]==0:
        ans.append(i)
    elif a[i]==0 and b[i]>0:
        ans.append(i)
print(*ans)
