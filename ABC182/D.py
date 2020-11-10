cur = 0
n = int(input())
A = list(map(int,input().split()))
S = [0]
for a in A:
    S.append(S[-1]+a)
S= S[1:]
T = [0]
for s in S:
    T.append(T[-1]+s)
T = T[1:]
ans = max(0,T[0])
U = [S[0]]
for i in range(1,len(S)):
    U.append(max(U[-1],S[i]))
for i in range(1,len(T)-1):
    ans = max(ans,T[i]+U[i-1])
ans = max(ans,T[-1])
# print(T,S,U)
print(ans)
