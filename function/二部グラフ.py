def nibu(n,g):
    from collections import deque
    q = deque([(0,0)])
    color = [-1]*n
    color[0] = 0
    while q:
        x,c = q.popleft()
        for y in g[x]:
            if color[y]==c:
                return False,[]
            if color[y]==-1:
                color[y]=1-c
                q.append((y,1-c))
    return True,color