a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
if b==a: print('YES');exit()
if v-w<=0:print('NO');exit()
dist = abs(b-a)
velocity = v-w
if dist/velocity <=t:print('YES')
else: print('NO')

