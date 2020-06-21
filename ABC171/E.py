import collections
N = int(input())
A = list(map(int,input().split()))
S = collections.deque([])
for i in range(1,N):
    S.append(A[i]^A[i-1])
val = A[0]
for i in range(0,len(S),2):
    val = val^S[i]
T = [str(val)]
while len(S)>0:
    T.append(str(int(T[-1])^S.popleft()))
print(' '.join(T))
    
