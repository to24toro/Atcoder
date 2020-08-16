s = input()
cnt = s.count('R')
if cnt != 2:
    print(cnt)
elif s[1] =='S':
    print(1)
else:
    print(2)