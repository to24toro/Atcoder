n = int(input())
L = []
for _ in range(n):
    a,b,c,d,e = map(int,input().split())
    L.append([a,b,c,d,e])
ans = 0

def check(x):
    s = set()
    for l in L:
        s.add(sum(1<<i for i in range(5) if l[i]>=x))
    for x in s:
        for y in s:
            for z in s:
                if x|y|z==31:
                    return True
    return False

left,right= 0,10**9+1
while right-left>1:
    mid = (right+left)//2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)



# for aa in range(2):
#     M = [0]*5
#     M[0]=aa
#     for bb in range(2):
#         M[1]=bb   
#         for cc in range(2):
#             M[2]=cc
#             for dd in range(2):
#                 M[3]=dd
#                 for ee in range(2):
#                     M[4]=ee
#                     tmp = 0
#                     for idx,l in enumerate(L):
#                         res = float('inf')
#                         for m,mm in enumerate(M):
#                             if mm:
#                                 if res>l[m]:
#                                     res = l[m]
#                         if tmp<res:
#                             tmp = max(tmp,res)
#                             iii = idx
#                     for b in range(1<<5):
#                         K = [0]*5
#                         for j in range(5):
#                             if (b>>j)&1:
#                                 K[j]=1
                        
#                         for p in range(5):
#                             if K[p]>0 and M[p]>0:
#                                 break
#                         else:
#                             tmp2 = 0
#                             for idx,l in enumerate(L):
#                                 res = float('inf')
#                                 if idx==iii:
#                                     continue
#                                 for k,kk in enumerate(K):
#                                     if kk:
#                                         res = min(res,l[k])
#                                 if tmp2<res:
#                                     tmp2 = max(tmp2,res)
#                                     iiii = idx
#                         # if M ==[0,1,0,1,0]:
#                         #     print(iii,iiii,K,M,tmp,tmp2)
#                         tmp3 = 0
#                         for idx,l in enumerate(L):
#                             res = float('inf')
#                             if idx==iii or idx==iiii:
#                                 continue
#                             for z in range(5):
#                                 if K[z]==0 and M[z]==0:
#                                     res = min(res,l[z])
#                             tmp3 = max(tmp3,res)
#                 # print(M,K,tmp,tmp2,tmp3)
#                         ans = max(ans,min(tmp,tmp2,tmp3))
# print(ans)
