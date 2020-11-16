n,x =map(int,input().split())
k = n
v = 0
i = 1
ans =[k+1]*n
while v+i<x:
    v+=i
    ans[-i]=1
    i+=1

ans[-i] = k-(x-v)+1
print(k)
print(' '.join(map(str,ans)))