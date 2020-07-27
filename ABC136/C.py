n = int(input())
H = list(map(int,input().split()))
if n==1: print('Yes');exit()
H[0]-=1
for i in range(n-1):
    if H[i]>H[i+1]:
        print('No');exit()
    elif H[i]==H[i+1]:
        continue
    else:
        H[i+1]-=1
print('Yes')