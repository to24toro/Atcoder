n,k = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))
g = [[0]*(n) for _ in range(n)]
A = [n]*n
# for i in range(n):
#     tmp = 0
#     idx = i
#     cnt = 0
#     set_ =set()
#     while cnt<n:
#         if C[idx] not in set_:
#             tmp += C[idx]
#             set_.add(C[idx])
#             g[i][cnt] = tmp
#             idx = P[idx]-1
#             cnt += 1
#         else:
#             p = len(set_)
#             A[i] = p
#             break
ans = -float('inf')

for i in range(n):
    S = []
    idx = P[i]-1
    S.append(C[idx])
    while idx != i:
        idx = P[idx]-1
        S.append(S[-1] +C[idx])
    v,w = k//len(S),k%len(S)
    if k<=len(S):
        val = max(S[:k])
    elif S[-1]<=0:
        val = max(S)
    else:
        val1 = S[-1] *(v-1)
        val1 += max(S)
        val2 = S[-1]*v
        if w!=0:
            val2 += max(0,max(S[:w]))
        val = max(val1,val2)
    ans = max(ans,val)
# for i in range(n):
#     v,w = k//A[i],k%A[i]
#     if A[i]<k:
#         if g[i][A[i]-1]<=0:
#             val = max(g[i][:A[i]])
#         else:
#             val1 = (v-1)*g[i][A[i]-1]
#             val1 += max(g[i][:A[i]])
#             val2 = v*g[i][A[i]-1]
#             if w!=0:
#                 val2 += max(0,max(g[i][:w]))
#             val = max(val1,val2)
#     else:
#         val = max(g[i][:k])
#     ans = max(ans,val)
print(ans)