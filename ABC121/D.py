A,B = map(int,input().split())
if A==0:
    fa = 0
else:
    v = (A-1)%4
    fa = 1 if v==2 or v ==1 else 0
    fa = fa ^ (A-1) if v%2==0 else fa
if B==0:
    fb = 0
else:
    v = (B)%4
    fb = 1 if v==2 or v ==1 else 0
    fb = fb ^ B if v%2==0 else fb
print(fa ^ fb)