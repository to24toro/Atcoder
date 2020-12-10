n = int(input())
P = list(map(lambda x: int(x)-1,input().split()))
cnt =0
A = []
# for i,p in enumerate(P):
#     if p==i:
#         if cnt == 0:
#             A.append(p-i)
#         else:
#             print(-1);exit()
#     else:
#         cnt += p-i
#         A.append(p-i)
# if cnt !=0:
#     print(-1);exit()
# else:
ans = []
B = []
for i in range(1,n):
    j = i-1
    ele = P[i]
    while P[j]>ele and j>=0:
        P[j+1] = P[j]
        ans.append(j)
        B.append(j)
        if len(ans)>n-1:
            print(-1);exit()
        j-=1
    P[j+1] = ele
A = [i+1 for i in range(n)]
B.sort()
if len(B)!=n-1:
    print(-1);exit()
for i in range(n-1):
    if B[i]+1!=A[i]:
        print(-1);exit()

for i in range(n):
    if A[i]!=P[i]+1:
        print(-1);exit()

for a in ans:
    print(a+1)