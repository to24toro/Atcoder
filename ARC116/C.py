n = int(input())
A = list(map(int,input().split()))
p = A[0]
ans = 0
cnt = 1
for i in range(1,n):
    if p==A[i]:
        cnt += 1
    else:
        if cnt%2==0:
            ans += (cnt//2)**2
            cnt = 1
        else:
            cnt-=1
            ans += cnt*(cnt+1)
            cnt = 1
        p = A[i]
        print(p,ans,i)
B = [(A[0],1)]
p = A[0]
cnt = 1
for i in range(1,n):
    if p!=A[i]:
        B.append((A[i],cnt))
        p = A[i]
        cnt = 1
    else:
        cnt += 1
for i in range(1,len(B)-1):
    if B[i][0]==B[i-1][0]+B[i+1][0]:
        ans += (B[i-1][1]//2)*(B[i+1]//2)

C = []
cnt = 0
p = A[0]
for i in range(1,n):
    if p!=A[i]:
        if cnt!=0:
            cnt = 0
            p = A[i]
        else:
            C.append(p)
            p = A[i]
            cnt = 0
    else:
        cnt += 1
if p!=C[-1]:
    C.append(p)
p = -float('inf')
cnt = 1
for i in range(1,len(C)-1):
    tmp = C[i]-C[i-1]-C[i+1]
    if tmp>0:
        if tmp==p:
            cnt += 1
        else:
            if cnt%2==0:
                ans += (cnt//2)**2
                cnt = 0
            else:
                cnt-=1
                ans += cnt*(cnt+1)
            p = tmp
            cnt = 1
if cnt>1:
    if cnt%2==0:
        ans += (cnt//2)**2
        cnt = 0
    else:
        cnt-=1
        ans += cnt*(cnt+1)
print(ans)