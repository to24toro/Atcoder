n = int(input())
S = input()
cnt = 0
i,j = 0,n-1
while i<j:
    if S[i]=='R' and S[j]=='R':
        i+=1
    elif S[i]=='R' and S[j]=='W':
        i += 1
        j -=1
    elif S[i]=='W' and S[j]=='W':
        j-=1
    else:
        cnt += 1
        i+=1
        j-=1
print(cnt)
