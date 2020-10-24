a,b,c,d = map(int,input().split())
s  =max(a,c)
t = min(b,d)
if s>=t:print(0)
else:
    print(t-s)