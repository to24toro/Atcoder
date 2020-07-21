n,m = map(int,input().split())
d = {}
f = True
if n ==1 and m==0: print(0);exit()

for i in range(m):
    s,c = map(int,input().split())
    if s-1 in d and d[s-1] != c:
        f = False
    d[s-1] = c
if not f: print(-1);exit()
l = ['-1']*n
for key,val in d.items():
    l[key] = str(val)
if n==1 and l[0]=='0':print(0);exit()
if l[0]=='0':print(-1);exit()
f = True
for i in range(len(l)):
    if l[0] == '-1':
        l[0]='1'
    elif l[i]=='-1':
        l[i]='0'
print(''.join(l))
            