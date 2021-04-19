
N=int(input())
aa=input()
ab=input()
ba=input()
bb=input()
MOD =10**9+7
 
F=[1,1]
for _ in range(1000):
    F.append((F[-1]+F[-2])%MOD)
             
if N==2:
    print(1)
    exit()
 
if (aa=='A' and ab=='A') or (ab=='B' and bb=='B'):
    print(1)
    exit()
    
if aa+ab+ba+bb in ['ABAA','BABA','BABB','BBAA']:
    print(pow(2,N-3,MOD))
    exit()
    
print(F[N-2])