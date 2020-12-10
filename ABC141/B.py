odd = {'R','U','D'}
even = {'L','U','D'}
S = input()
for i in range(len(S)):
    if i%2:
        if S[i] in even:
            continue
        else:
            print('No');exit()
    else:
        if S[i] in odd:
            continue
        else:
            print('No');exit()
print('Yes')
