n,t = map(int,input().split())
A = list(map(int,input().split()))
b = float('inf')
B = []
for a in A:
    b = min(b,a)
    B.append(a-b)
B.sort()
cnt = B.count(B[-1])
print(cnt)
