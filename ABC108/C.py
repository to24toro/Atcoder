n,k = map(int,input().split())
cnt = 0
cnt2 = 0

for i in range(1,n+1):
    if i%k==0:
        cnt += 1
    elif k%2==0 and i%k==k//2:
        cnt2+=1
print(cnt**3+cnt2**3)