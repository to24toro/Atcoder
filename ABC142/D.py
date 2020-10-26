import math
A,B = map(int,input().split())
a = []
b = []
for i in range(1,int(A**0.5)+1):
    if A%i==0:
        a.append(i)
        if i!=A//i:
            a.append(A//i)

for i in a:
    if B%i==0: b.append(i)
b.sort()
ans = [1]*len(b)
for i in range(1,len(b)):
    if ans[i]:
        for j in range(i+1,len(b)):
            if b[j]%b[i]==0:
                ans[j]=0
print(sum(ans))