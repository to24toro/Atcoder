n = int(input())
A = list(map(int,input().split()))
d = []
for i,x in enumerate(A):
    d.append((x,str(i+1)))
d.sort()
ans= []
for x,i in d:
    ans.append(i)

print(' '.join(ans))