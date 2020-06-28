N = int(input())
A = list(map(int,input().split()))
B = [[A[i],i] for i in range(N)]
d = {}
B.sort()
for i in range(N):
    d[B[i][1]] = i
for i in range(N):
    if d[i] <N//2:
        print(B[N//2][0])
    else:
        print(B[-1+(N//2)][0])