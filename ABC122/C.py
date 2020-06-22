N,Q = map(int,input().split())
S = input()

T = []
count = 0
idx = -1
for i,s in enumerate(S):
    if s =='C' and idx ==i-1:
        idx = -1
        count += 1
    elif s =='A':
        idx = i
    T.append(count)
q = []
for _ in range(Q):
    l,r = map(int,input().split())
    q.append([l,r])
for l,r in q:
    print(T[r-1]-T[l-1])