T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int,input().split())))
    A.sort(key = lambda x:(x[0],x[1]>x[2],-x[1]))
    print(A)
