l,h = map(int,input().split())
n = int(input())
for _ in range(n):
    a = int(input())
    if a>=l and h>=a:
        print(0)
    elif l>a:
        print(l-a)
    else:
        print(-1)