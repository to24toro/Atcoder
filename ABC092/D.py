A,B  =map(int,input().split())
K = 50
S = [['.']*(2*K) for _ in range(2*K)]
for i in range(K):
    for j in range(2*K):
        S[i][j] ='#'
i,j = 0,0
A-=1
B-=1
while A>0:
    S[i][j] ='.'
    if j +2 <2*K:
        j +=2
    else:
        i += 2
        j=0
    A-=1
i,j = 2*K-1,2*K-1
while B>0:
    S[i][j]='#'
    if j-2>0:
        j-=2
    else:
        i-=2
        j=2*K-1
    B-=1
print(str(2*K)+' '+str(2*K))
for s in S:
    print(''.join(s))