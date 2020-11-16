S  = input()
n = len(S)
for i in range(26):
    x = chr(int(ord('a')+i))
    s,t = 0,0
    cnt = 0
    while t<n:
        if S[t]==x:
            t += 1
            cnt += 1
            if t-s+1<2*cnt and t-s+1>=2:
                print(s+1,t);exit()
        else:
            if t-s+1<2*cnt and t-s+1>=2:
                print(s+1,t+1);exit()
            else:
                if t+1<n and t-s+1>=2:
                    if S[t+1]!=x:
                        t += 1
                        s = t
                        cnt = 0
                    else:
                        t += 1
                        cnt += 1
                else:
                    t += 1
                    s = t
                    cnt = 0
print(-1,-1)