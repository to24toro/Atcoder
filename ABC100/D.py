N,M = map(int,input().split())
P = []
for _ in range(N):
    x,y,z = map(int,input().split())
    P.append([x,y,z])
ans = 0
for X in(1,-1):
    for Y in (1,-1):
        for Z in (1,-1):
            A = []
            for i in range(len(P)):
                val = X*P[i][0] + Y*P[i][1] + Z*P[i][2]
                A.append(val)
            A.sort(reverse = True)
            ans = max(ans,sum(A[:M]))
print(ans)
#O(NlogN)ă§ćšćæ