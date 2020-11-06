# mod = 10**9 + 7
# h, w = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(h)]
# g = [[-1] * w for _ in range(h)]
# d = ((1, 0), (-1, 0), (0, 1), (0, -1))
# ans = 0
# def dfs(x, y):
#         if g[x][y] >= 0:
#             return g[x][y]
 
#         cnt = 1
#         base = a[x][y]
#         for dx, dy in d:
#             if 0 <= x+dx < h and 0 <= y+dy < w and base < a[x+dx][y+dy]:
#                 cnt += dfs(x+dx, y+dy)
#         cnt %= mod
#         g[x][y] = cnt
#         return cnt
# ans = 0  
# for i in range(h):
#   for j in range(w):
#     ans += dfs(i, j)
#     ans %= mod
# print(ans % mod)
mod = 10**9 + 7
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

g = [[-1] * w for _ in range(h)]

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs(x, y):
    if g[x][y] >= 0:
        return g[x][y]

    cnt = 1
    base = a[x][y]
    for dx, dy in dxy:
        if 0 <= x+dx < h and 0 <= y+dy < w and base < a[x+dx][y+dy]:
            cnt += bfs(x+dx, y+dy)
    cnt %= mod
    g[x][y] = cnt
    return cnt

ans = 0
for x in range(h):
    for y in range(w):
        ans += bfs(x, y)
    ans %= mod
print(ans)