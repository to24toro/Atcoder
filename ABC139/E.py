from collections import deque

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
Q = [deque([]) for _ in range(n)]
for i in range(n):
    for a in A[i]:
        Q[i].append(a-1)
day = 0
cnt = 0
D = [0]*n
match = n*(n-1)//2
L = list(range(n))
while match>0:
    cnt = 0
    pre = match
    LL = []
    for i in L:
        if Q[i]:
            a = Q[i].popleft()
            if Q[a][0]==i:
                Q[a].popleft()
                D[i] = max(D[i],D[a])
                D[a] = D[i]
                D[i] +=1
                D[a] += 1
                match-=1
                LL.append(i)
                LL.append(a)
            else:
                Q[i].appendleft(a)
    LL.sort()
    L = LL
    if pre==match:
        print(-1);exit()

ans = 0
for i in range(n):
    if Q[i]:
        print(-1);exit()
    ans = max(ans,D[i])
print(ans);exit()


# q = deque([i for i in range(n)])
# cur_day = [0]*n
# cnt = [0]*n
# for _ in range(10**6+100000):
#     if not q:break
#     p = q.popleft()
#     day = cur_day[p]
#     match = cnt[p]
#     pre_match = match
#     while match<n-1 and p==L[L[p][match]][cnt[L[p][match]]]:
#         day = max(cur_day[p],cur_day[L[p][match]])
#         day+=1
#         cur_day[p]= day
#         cur_day[L[p][match]]=day
#         cnt[L[p][match]]+=1
#         cnt[p]+=1
#         match+=1
#         # print(cnt,cur_day,p)
#     if match<n-1:
#         q.append(p)
# # print(cnt,cur_day)
# for c in cnt:
#     if c!=n-1:
#         print(-1);exit()
# print(max(cur_day))