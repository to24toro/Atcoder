A,B,C,K = map(int,input().split())
if A>=K: print(K)
else:
    K-=A
    if B>=K: print(A)
    else:
        K-=B
        print(A-K)