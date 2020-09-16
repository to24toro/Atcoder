n = int(input())
T  =list(map(int,input().split()))
s =sum(T)
m = int(input())
ans = []
for _ in range(m):
    p,x = map(int,input().split())
    ans.append(s-T[p-1]+x)
for a in ans:
    print(a)