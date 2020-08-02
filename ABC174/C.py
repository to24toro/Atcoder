k = int(input())
dp =[0]
for i in range(10**6+1):
    dp.append((dp[-1]*10+7)%k)
    if dp[-1]==0:print(i+1);exit()
print(-1)