N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
if N>=M: print(0);exit()
if N==1: print(X[-1]-X[0]);exit()
L = []
for i in range(len(X)-1):
    L.append(X[i+1]-X[i])
L.sort()
L = L[:-(N-1)]
print(sum(L))