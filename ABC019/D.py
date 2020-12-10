N = int(input())
edge = []
for i in range(2,N+1):
    print('?',1,i)
    l = int(input())
    edge.append((l,i))
edge.sort(reverse=True)
ans,v = edge[0]
for j in range(1,N-1):
    nv = edge[j][1]
    print('?',v,nv)
    cnt = int(input())
    ans= max(ans,cnt)
print('!',ans)