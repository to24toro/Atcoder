t = int(input())
a = 'atcoder'
T = []
for _ in range(t):
    T.append(input())
for s in T:
    if len(s)==s.count('a'):
        print(-1);
    elif s[:7]=='atcoder':
        if len(s)>7:
            print(0)
        else:
            print(1)
    else:
        if len(a)<=len(s):
            f = False
            for i in range(len(a)):
                if ord(a[i])>ord(s[i]):
                    break
                elif ord(a[i])<ord(s[i]):
                    print(0)
                    f = True
                    break
            if not f:
                for i in range(len(s)):
                    if s[i]!='a':
                        if ord(s[i])>ord('t'):
                            print(i-1);break
                        else:
                            print(i);break
        else:
            f = False
            for i in range(len(s)):
                if ord(a[i])>ord(s[i]):
                    break
                elif ord(a[i])<ord(s[i]):
                    print(0)
                    f = True
                    break
            if not f:
                for i in range(len(s)):
                    if s[i]!='a':
                        if ord(s[i])>ord('t'):
                            print(i-1);break
                        else:
                            print(i);break