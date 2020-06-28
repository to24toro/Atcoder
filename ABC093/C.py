A,B,C = map(int,input().split())
a = max(A,B,C)
c = min(A,B,C)
b = A+B+C-a-c
ans = a-b
if (b-c)%2==0:
    print(ans + (b-c)//2)
else:
    print(2 + ans + (b-c)//2)