n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
s = sum(B)-sum(A)
if s<0:
    print('No');exit()
t = 0
for a,b in zip(A,B):
    if a<=b:
      if (b-a)%2==1:
          s-=1
    else:
        s-=(a-b)
if s>=0:
    print('Yes')
else:
    print('No')