n = int(input())
cnt = 0
for i in range(1,n+1):
    l = len(str(i))
    if l%2==1:
        cnt += 1
print(cnt)