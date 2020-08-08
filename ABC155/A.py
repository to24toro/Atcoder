a,b,c = map(int,input().split())
if (a==b and a!=c) or (c==b and a!=c) or (a==c and a!=b):
    print('Yes')
else:
    print('No')