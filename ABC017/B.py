s = input()
n = len(s)
i = 0
while i<n:
    if s[i] =='c':
        if i+1<n and s[i+1]=='h':
            i+=2
        else:
            print('NO');exit()
    elif s[i]=='o' or s[i]=='k' or s[i]=='u':
        i+=1
    else:
        print('NO');exit()
print('YES')
