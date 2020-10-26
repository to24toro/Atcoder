n,k = map(int,input().split())
H = list(map(int,input().split()))
cnt = 0
for h in H:
    if h>=k:cnt+=1
print(cnt)