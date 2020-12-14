n = int(input())
S = input()
cnt = 0
for s in S:
    if s=='A':
        cnt += 4
    elif s=='B':
        cnt += 3
    elif s=='C':
        cnt += 2
    elif s=='D':
        cnt += 1
    else:
        cnt += 0
print(cnt/n)