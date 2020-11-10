n = int(input())
A = list(map(int,input().split()))
ans  =[0]*(max(A)+1)
for x in range(2,max(A)+1):
    for a in A:
        if a%x==0:
            ans[x]+=1
res = max(ans)
for i,a in enumerate(ans):
    if a==res:
        print(i);exit()

