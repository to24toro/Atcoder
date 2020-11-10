n = int(input())
A = list(map(int,input().split()))
ans = -float('inf')
for i in range(n):#一つ選んで
    a = []
    t = []
    for j in range(n):#すべての他の点に対して数列を考えて点数を考える
        if i==j:
            continue
        l = A[min(i,j):max(i,j)+1]
        a.append(sum(l[1::2]))
        t.append(sum(l[::2]))
    ans = max(ans,t[a.index(max(a))])#その中での最大の時のj

print(ans)