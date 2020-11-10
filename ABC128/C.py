# n,m = map(int,input().split())
# A = []
# ans = 0
# for _ in range(m):
#     A.append(list(map(int,input().split())))
# P = list(map(int,input().split()))
# for bit in range(1<<n):
#     flag = True
#     for i in range(m):
#         cnt = 0
#         k,S = A[i][0],A[i][1:]
#         for s in S:
#             if ((bit>>(s-1))&1) and flag == True:
#                 cnt += 1
#         if cnt %2==P[i]:
#             continue
#         else:
#             flag = False
#     if flag:
#         ans += 1
# print(ans)

n,m = map(int,input().split())
A  =[]
ans = 0
for _ in range(m):
    A.append(list(map(int,input().split())))
P = list(map(int,input().split()))
for bit in range(1<<n):
    count = 0
    for i in range(m):
        p = P[i]
        k,S = A[i][0],A[i][1:]
        cnt = 0
        for s in S:
            if (bit>>(s-1))&1:
                cnt += 1
        if p==cnt%2:
            count += 1
    if count ==m:
        ans += 1
print(ans)












