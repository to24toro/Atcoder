n = int(input())
S = input()
L  =[s for s in S]
M = []
for s in S:
    if s!='x':
        M.append(s)
    else:
        if len(M)>1 and M[-1]=='o' and M[-2]=='f':
            M.pop()
            M.pop()
        else:
            M.append(s)
print(len(M))