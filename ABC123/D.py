x,y,z,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ma = max(A)
mb = max(B)
mc = max(C)
L = [a+b for a in A for b in B]
L.sort(reverse=True)
L = L[:k]
L = [l+c for c in C for l in L]
L.sort(reverse=True)
L = L[:k]
print(*L,sep='\n')