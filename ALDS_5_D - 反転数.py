n = int(input())
A = list(map(int,input().split()))
data = [0]*(n+1)
d = {}
for i,a in enumerate(sorted(A)):
    d[a]=i
B = []
for a in A:
    B.append(d[a]+1)
def add(k,v):
    while k<=n:
        data[k] += v
        k += k&-k
def get(k):
    s = 0
    while k:
        s += data[k]
        k-=k&-k
    return s
ans =0
# print(B)
for i,b in enumerate(B):
    add(b,1)
    ans += i+1-get(b)
print(ans)
