N,Y = map(int,input().split())
for a in range(N+1):
    for b in range(N+1):
        val = Y-10000*a-5000*b
        n = N-a-b
        if n>=0 and val >=0 and n*1000==val:
            print(a,b,N-a-b);exit()
print('-1 -1 -1')