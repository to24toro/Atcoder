s= input()
t = input()
set_ = {'a','t','c','d','o','e','r'}
for i in range(len(t)):
    if s[i]==t[i]:
        continue
    else:
        if s[i]=='@' and t[i] in set_:
            continue
        elif t[i]=='@' and s[i] in set_:
            continue
        else:
            print('You will lose');exit()
print('You can win')
