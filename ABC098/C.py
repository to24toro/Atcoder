N = int(input())
S = input()
W=[0]*(N+1)
E=[0]*(N+1)
a=0
b=0
for i in range(N):
  if S[i]=='W':
    a+=1
  else:
    b+=1
  W[i+1]=a
  E[i+1]=b

ans = float('inf')
for i in range(1,N+1):
    ans = min(W[i-1] + E[N]-E[i],ans)
print(ans)