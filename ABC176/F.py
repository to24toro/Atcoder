n = int(input())
A = list(map(int,input().split()))
A.sort()
from collections import deque,defaultdict
dic = defaultdict(int)
cnt = 0
for a in A:
    dic[a] +=1
def helper(A,cnt):
    A.sort()
    if A[0]==A[2]:
        cnt += 1
        return A[3:],cnt
    elif A[2]==A[-1]:
        cnt += 1
        return A[:2],cnt
    tmp = []
    q = deque([])
    for a in A:
        if dic[a]%3==1:
            q.append(a)
        if dic[a]%3==2:
            q.appendleft(a)
        else:
            tmp.append(a)
    ans = tmp + q
    return ans[:2],cnt
for _ in range(n-1):
    a = A[:5]
    B = A[5:]
    ans,cnt = helper(a,cnt)
    A = ans + B
A.sort()
print(cnt+1 if A[0]==A[-1] else cnt)