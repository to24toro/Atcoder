n = int(input())
L = []
for _ in range(n):
    x,y = map(int,input().split())
    L.append((x+y,x,y))
L.sort(key = lambda x:-x[0])
