n = int(input())
L = [tuple(map(int,input().split())) for _ in range(n)]
Z = [x+y for x,y in L]
W = [x-y for x,y in L]
Z.sort()
W.sort()
print(max(Z[-1]-Z[0],W[-1]-W[0]))